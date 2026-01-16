document.addEventListener('DOMContentLoaded', function() {
    const iconContainers = document.querySelectorAll('.icon-container');
    iconContainers.forEach(container => {
        container.addEventListener('click', function() {
            this.style.transform = 'translateY(-8px) scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'translateY(-8px)';
            }, 150);
        });
    });
});
