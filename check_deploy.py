#!/usr/bin/env python3
"""
Poll GitHub Deployments API to detect when a GitHub Pages deploy has completed.

Usage:
  python3 check_deploy.py <commit_sha>
    e.g. python3 check_deploy.py c21d38a

  Optionally also verifies a string is live on the site after deploy:
  python3 check_deploy.py <commit_sha> <expected_string> [<url>]
    e.g. python3 check_deploy.py c21d38a "PLY_abc123" "https://theflip.top/posts/005-nobodys-charts.html"

Exits 0 when deployed (and string found, if given), 1 on timeout.
"""
import sys
import time
import json
import urllib.request

REPO = "michaelgpearce/mike2000"
ENVIRONMENT = "github-pages"
MAX_WAIT = 300   # 5 minutes
POLL_INTERVAL = 15

commit_sha = sys.argv[1] if len(sys.argv) > 1 else None
expect_string = sys.argv[2] if len(sys.argv) > 2 else None
check_url_override = sys.argv[3] if len(sys.argv) > 3 else None

if not commit_sha:
    print("Usage: check_deploy.py <commit_sha> [expected_string] [url]")
    sys.exit(1)

def api_get(url):
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "mike2000-deploy-check",
                "Accept": "application/vnd.github+json",
            },
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as e:
        return None

def get_deployment_status(sha):
    """
    Returns 'success', 'failure', 'pending', or None if not found.
    Checks deployments matching the SHA (full or short) in the github-pages env.
    """
    url = f"https://api.github.com/repos/{REPO}/deployments?environment={ENVIRONMENT}&per_page=10"
    deployments = api_get(url)
    if not deployments:
        return None

    # Match on full or short SHA
    matched = [d for d in deployments if d.get("sha", "").startswith(sha) or sha.startswith(d.get("sha", "")[:7])]
    if not matched:
        return None

    deployment_id = matched[0]["id"]
    statuses_url = f"https://api.github.com/repos/{REPO}/deployments/{deployment_id}/statuses"
    statuses = api_get(statuses_url)
    if not statuses:
        return "pending"

    # Most recent status is first
    return statuses[0].get("state", "pending")

def check_string_live(url, expect):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "mike2000-deploy-check"})
        with urllib.request.urlopen(req, timeout=10) as r:
            if r.status == 200:
                body = r.read().decode("utf-8", errors="ignore")
                return expect in body
    except Exception:
        pass
    return False

print(f"Waiting for deploy of {commit_sha} to {ENVIRONMENT}...")

start = time.time()
while time.time() - start < MAX_WAIT:
    elapsed = int(time.time() - start)
    status = get_deployment_status(commit_sha)

    if status == "success":
        print(f"  [{elapsed}s] ✓ Deployment succeeded")
        if expect_string and check_url_override:
            print(f"  Verifying '{expect_string}' is live at {check_url_override}...")
            if check_string_live(check_url_override, expect_string):
                print(f"✓ LIVE after {elapsed}s")
                sys.exit(0)
            else:
                print(f"  [{elapsed}s] deploy done but string not found yet, retrying...")
        else:
            print(f"✓ LIVE after {elapsed}s")
            sys.exit(0)
    elif status == "failure":
        print(f"✗ Deployment failed after {elapsed}s")
        sys.exit(1)
    elif status is None:
        print(f"  [{elapsed}s] no deployment found yet, retrying in {POLL_INTERVAL}s...")
    else:
        print(f"  [{elapsed}s] status={status}, retrying in {POLL_INTERVAL}s...")

    time.sleep(POLL_INTERVAL)

print(f"✗ Timeout after {MAX_WAIT}s — deploy may still be in progress")
sys.exit(1)
