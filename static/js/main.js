(function () {
  var header = document.getElementById('header');
  var burger = document.querySelector('.burger');
  var nav = document.getElementById('nav');

  function onScroll() { header.classList.toggle('scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  burger.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });

  // Cookie notice
  var banner = document.getElementById('cookie');
  var accepted = false;
  try { accepted = localStorage.getItem('cookieOk') === '1'; } catch (e) {}
  if (!accepted) banner.hidden = false;
  document.getElementById('cookie-ok').addEventListener('click', function () {
    try { localStorage.setItem('cookieOk', '1'); } catch (e) {}
    banner.hidden = true;
  });

  // Scroll reveal
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: .12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Menu: highlight the category being read
  var links = document.querySelectorAll('.menu-nav a');
  if (links.length && 'IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          links.forEach(function (a) { a.classList.toggle('active', a.getAttribute('href') === '#' + e.target.id); });
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    document.querySelectorAll('.menu-cat').forEach(function (s) { spy.observe(s); });
  }

  // Gallery lightbox
  var box = document.getElementById('lightbox');
  if (box && box.showModal) {
    var img = box.querySelector('img'), cap = box.querySelector('p');
    document.querySelectorAll('[data-full]').forEach(function (b) {
      b.addEventListener('click', function () {
        img.src = b.dataset.full; img.alt = b.dataset.title; cap.textContent = b.dataset.title;
        box.showModal();
      });
    });
    box.addEventListener('click', function (e) { if (e.target === box || e.target.classList.contains('close')) box.close(); });
  }
})();
