const themeToggleBtn = document.getElementById('theme-toggle');

const updateIcon = () => {
    if (document.documentElement.classList.contains('dark')) {
        themeToggleBtn.textContent = 'dark_mode';
    } else {
        themeToggleBtn.textContent = 'light_mode';
    }
};

// Sync icon with the class that was already applied by the inline head script
updateIcon();

themeToggleBtn.addEventListener('click', function () {
    const isDark = document.documentElement.classList.contains('dark');

    if (isDark) {
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

(function () {
                var stored = localStorage.getItem('theme');
                var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                var isDark = stored === 'dark' || (!stored && prefersDark);
                document.documentElement.classList.toggle('dark', isDark);
                document.documentElement.classList.toggle('light', !isDark);
            })();

        setTimeout(() => {
        const toasts = document.querySelectorAll('.custom-toast');
        toasts.forEach((toast) => {
            toast.remove();
        });
        }, 6000);