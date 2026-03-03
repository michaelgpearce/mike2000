// Shared header/footer for The Flip
// Detects depth so relative paths work from both root and /posts/

(function () {
  const isPost = window.location.pathname.includes('/posts/');
  const root = isPost ? '../' : '';

  const header = `
    <header>
      <div class="header-inner">
        <h1><a href="${root}index.html">THE FLIP</a></h1>
        <div class="header-tags">
          <span>Garage</span><span>Beat</span><span>Bubblegum</span><span>Glam</span><span>Punk</span><span>Powerpop</span>
        </div>
        <p class="header-sub">Songs worth sharing &mdash; some you know, some you don't, all of them great.</p>
      </div>
    </header>`;

  const footer = `
    <footer>
      <p>THE FLIP &mdash; weekly music you should've heard by now</p>
    </footer>`;

  document.getElementById('site-header').innerHTML = header;
  document.getElementById('site-footer').innerHTML = footer;
})();
