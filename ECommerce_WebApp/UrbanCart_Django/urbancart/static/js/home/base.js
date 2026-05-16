// Prevent flash of unstyled content
if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
    document.documentElement.classList.remove('light');
} else {
    document.documentElement.classList.remove('dark');
    document.documentElement.classList.add('light');
}

const themeToggleBtn = document.getElementById('theme-toggle');
            
const updateIcon = () => {
    if (document.documentElement.classList.contains('dark')) {
        themeToggleBtn.textContent = 'dark_mode';
    } else {
        themeToggleBtn.textContent = 'light_mode';
    }
};
                
updateIcon();

themeToggleBtn.addEventListener('click', function() {
    if (document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.remove('dark');
        document.documentElement.classList.add('light');
        localStorage.setItem('theme', 'light');
    } else {
        document.documentElement.classList.add('dark');
        document.documentElement.classList.remove('light');
        localStorage.setItem('theme', 'dark');
    }
    updateIcon();
});