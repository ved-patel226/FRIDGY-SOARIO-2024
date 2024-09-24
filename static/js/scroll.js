document.addEventListener('DOMContentLoaded', function() {
    const nav = document.querySelector('nav');

    window.addEventListener('scroll', function() {
        if (window.scrollY === 0) {
            nav.style.backgroundColor = 'transparent';
        } else {
            nav.style.backgroundColor = 'var(--primary-color)';
        }
    });
});
