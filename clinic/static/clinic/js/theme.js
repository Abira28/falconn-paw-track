/* Light and dark mode switch for the public site.
   The first choice is made by the small script in <head> (saved choice,
   otherwise the device setting). This file handles the button. */
(function () {
    'use strict';

    var html = document.documentElement;
    var button = document.querySelector('.theme-toggle');
    if (!button) { return; }

    function isDark() { return html.getAttribute('data-theme') === 'dark'; }

    function updateLabel() {
        var text = isDark() ? 'Switch to light mode' : 'Switch to dark mode';
        button.setAttribute('aria-label', text);
        button.setAttribute('title', text);
    }

    function setTheme(name, save) {
        html.setAttribute('data-theme', name);
        if (save) {
            try { localStorage.setItem('theme', name); } catch (e) { /* private mode */ }
        }
        updateLabel();
    }

    updateLabel();

    button.addEventListener('click', function () {
        html.classList.add('theme-anim');
        setTheme(isDark() ? 'light' : 'dark', true);
        setTimeout(function () { html.classList.remove('theme-anim'); }, 450);
    });

    // Until the visitor picks a mode, follow their device if it changes.
    if (window.matchMedia) {
        var query = window.matchMedia('(prefers-color-scheme: dark)');
        var follow = function (event) {
            var saved = null;
            try { saved = localStorage.getItem('theme'); } catch (e) { /* ignore */ }
            if (!saved) { setTheme(event.matches ? 'dark' : 'light', false); }
        };
        if (query.addEventListener) { query.addEventListener('change', follow); }
    }
})();
