/* ================================================================
   KHALIDA FOUNDATION — SHARED NAVBAR SCRIPT
   Handles: scroll-shrink, topbar hide, reading progress,
            mobile drawer, keyboard nav
   ================================================================ */
(function () {
    'use strict';

    /* ── Elements ─────────────────────────────────────────────── */
    var nav       = document.getElementById('kf-nav');
    var topbar    = document.getElementById('kf-topbar');
    var progress  = document.getElementById('kf-progress');
    var hamburger = document.getElementById('kfHamburger');
    var menu      = document.getElementById('kfMobileMenu');
    var overlay   = document.getElementById('kfOverlay');
    var closeBtn  = document.getElementById('kfMobileClose');

    /* ── Scroll handler ───────────────────────────────────────── */
    function onScroll() {
        var y = window.scrollY || window.pageYOffset;

        if (nav) nav.classList.toggle('kf-scrolled', y > 55);
        if (topbar) topbar.classList.toggle('kf-hidden', y > 75);

        if (progress) {
            var docH = document.documentElement.scrollHeight - window.innerHeight;
            var pct  = docH > 0 ? Math.min((y / docH) * 100, 100) : 0;
            progress.style.width = pct + '%';
        }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    /* ── Mobile drawer ────────────────────────────────────────── */
    function openMenu() {
        if (!menu || !hamburger) return;
        menu.classList.add('kf-open');
        if(overlay) overlay.classList.add('kf-open');
        hamburger.classList.add('kf-open');
        hamburger.setAttribute('aria-expanded', 'true');
        document.body.style.overflow = 'hidden';
        var first = menu.querySelector('a, button');
        if (first) setTimeout(function () { first.focus(); }, 340);
    }

    function closeMenu() {
        if (!menu || !hamburger) return;
        menu.classList.remove('kf-open');
        if(overlay) overlay.classList.remove('kf-open');
        hamburger.classList.remove('kf-open');
        hamburger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
        hamburger.focus();
    }

    if (hamburger) hamburger.addEventListener('click', openMenu);
    if (closeBtn)  closeBtn.addEventListener('click', closeMenu);
    if (overlay)   overlay.addEventListener('click', closeMenu);

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && menu && menu.classList.contains('kf-open')) closeMenu();
    });

    if (menu) {
        menu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', closeMenu);
        });
    }

    /* ── Desktop dropdown keyboard nav ───────────────────────── */
    var items = document.querySelectorAll('.kf-nav-links > li');
    items.forEach(function (li) {
        var trigger  = li.querySelector('.kf-link');
        var dropdown = li.querySelector('.kf-dropdown');
        if (!trigger || !dropdown) return;

        trigger.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' || e.key === ' ' || e.key === 'ArrowDown') {
                e.preventDefault();
                dropdown.classList.add('kf-open');
                trigger.setAttribute('aria-expanded', 'true');
                var first = dropdown.querySelector('a, [role="menuitem"]');
                if (first) first.focus();
            }
        });

        dropdown.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                dropdown.classList.remove('kf-open');
                trigger.setAttribute('aria-expanded', 'false');
                trigger.focus();
            }
        });

        document.addEventListener('click', function (e) {
            if (!li.contains(e.target)) {
                dropdown.classList.remove('kf-open');
                trigger.setAttribute('aria-expanded', 'false');
            }
        });
    });

})();
