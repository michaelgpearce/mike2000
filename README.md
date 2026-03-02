# Crate Digger

Underground music blog. 60s-80s garage, bubblegum, glam, punk, powerpop.

## Deploy to GitHub Pages

1. **Create a new repo on GitHub** (name it whatever, like `crate-digger` or `music-blog`)

2. **Initialize and push:**
```bash
cd /root/.openclaw/workspace/music-blog
git init
git add .
git commit -m "Initial commit: Week 1"
git branch -M main
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

3. **Enable GitHub Pages:**
   - Go to repo Settings → Pages
   - Source: Deploy from branch
   - Branch: `main` / `(root)`
   - Save

4. **Your site will be live at:**
   `https://YOUR_USERNAME.github.io/YOUR_REPO/`

## Adding New Posts

1. Create new HTML file in `posts/` (e.g., `002-title.html`)
2. Copy structure from `001-fizzed-out-psych.html`
3. Update `index.html` to add the new post preview at the top
4. Commit and push

## Structure

```
music-blog/
├── index.html          # Homepage with post list
├── css/
│   └── style.css       # Styling
├── posts/
│   └── 001-fizzed-out-psych.html
└── README.md
```

Simple. No Jekyll, no frameworks. Just HTML/CSS.
