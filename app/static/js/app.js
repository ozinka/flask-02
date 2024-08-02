function setThemeUI() {
    document.getElementById('select-theme-auto').classList.remove('active');
    document.getElementById('select-theme-light').classList.remove('active');
    document.getElementById('select-theme-dark').classList.remove('active');

    const theme = getPreferredTheme();
    document.getElementById('select-theme-' + theme).classList.add('active');

    const actualTheme = document.documentElement.getAttribute('data-bs-theme') || 'auto';
    document.getElementById('current-theme').setAttribute('href', `#icon-theme-${actualTheme}`);
}

function updateTheme(theme) {
    if (theme === 'auto') {
        localStorage.removeItem('theme');
    } else {
        localStorage.setItem('theme', theme);
    }
    setTheme(getPreferredTheme());
    setThemeUI();  // Ensure UI is updated after setting the theme
}

function getPreferredTheme() {
    const storedTheme = localStorage.getItem('theme');
    if (storedTheme) {
        return storedTheme;
    }
    return 'auto';
}

function setTheme(theme) {
    if (theme === 'auto') {
        theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    document.documentElement.setAttribute('data-bs-theme', theme);
    setThemeUI();  // Ensure UI is updated after setting the theme
}

document.addEventListener("DOMContentLoaded", () => {
    setTheme(getPreferredTheme());

    const darkModePreference = window.matchMedia("(prefers-color-scheme: dark)");
    darkModePreference.addEventListener("change", e => {
        if (getPreferredTheme() === 'auto') {
            setTheme('auto');
        }
    });

    // add prettyprint class to all <pre><code></code></pre> blocks
    let prettify = false;
    document.querySelectorAll('div.post-body pre code').forEach((code) => {
        code.parentNode.classList.add('prettyprint');
        prettify = true;
    });
    if (prettify) {
        prettyPrint();
    }
});
