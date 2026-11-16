/* PawTrack public site: sections fade up as you scroll, and a paw print
   appears where you tap. Skipped when the visitor prefers reduced motion. */
(function () {
    'use strict';

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        return;
    }

    /* 1. Fade up on scroll */
    var SELECTORS = [
        '.page-head .wrap > *',
        '.section h2',
        '.section .intro',
        '.svc li',
        '.steps li',
        '.principle',
        '.acc-item',
        '.prose > *',
        '.band-grid > div',
        '.form-panel',
        '.aside-list li',
        '.map iframe',
        '.foot-grid > div'
    ].join(',');

    if ('IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('in');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

        document.querySelectorAll(SELECTORS).forEach(function (el) {
            var position = el.parentElement
                ? Array.prototype.indexOf.call(el.parentElement.children, el)
                : 0;
            el.classList.add('reveal');
            el.style.transitionDelay = Math.min(position, 5) * 70 + 'ms';
            el.addEventListener('transitionend', function clear() {
                el.style.transitionDelay = '';
                el.removeEventListener('transitionend', clear);
            });
            observer.observe(el);
        });
    }

    /* 2. Paw print where you tap */
    var PAW = '<svg viewBox="0 0 32 32" aria-hidden="true">' +
        '<ellipse cx="6" cy="14" rx="3.2" ry="4.4"/><ellipse cx="12.5" cy="7.5" rx="3.2" ry="4.6"/>' +
        '<ellipse cx="21" cy="7.5" rx="3.2" ry="4.6"/><ellipse cx="27" cy="14" rx="3.2" ry="4.4"/>' +
        '<path d="M16 15c-5 0-9 4-9 8 0 3 2.5 4 5 4 2 0 3-1 4-1s2 1 4 1c2.5 0 5-1 5-4 0-4-4-8-9-8z"/></svg>';

    document.addEventListener('click', function (event) {
        // Keyboard activations report 0,0, and form fields should stay calm.
        if ((event.clientX === 0 && event.clientY === 0) ||
            event.target.closest('input, textarea, select')) {
            return;
        }
        var paw = document.createElement('span');
        paw.className = 'paw-tap';
        paw.setAttribute('aria-hidden', 'true');
        paw.innerHTML = PAW;
        paw.style.left = event.clientX + 'px';
        paw.style.top = event.clientY + 'px';
        paw.style.setProperty('--tilt', Math.round(Math.random() * 50 - 25) + 'deg');
        document.body.appendChild(paw);
        paw.addEventListener('animationend', function () { paw.remove(); });
    });
})();
