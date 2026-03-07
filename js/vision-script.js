document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const zoomBtn = document.querySelector('.zoom-btn');
    const imageModal = document.getElementById('imageModal');
    const modalClose = document.querySelector('.modal-close');

    navToggle?.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });

    document.querySelectorAll('.nav-menu a').forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
        });
    });

    zoomBtn?.addEventListener('click', () => {
        imageModal.classList.add('active');
    });

    modalClose?.addEventListener('click', () => {
        imageModal.classList.remove('active');
    });

    imageModal?.addEventListener('click', (e) => {
        if (e.target === imageModal) {
            imageModal.classList.remove('active');
        }
    });

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('.facility-card, .detail-card, .allocation-item').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    const allocationBars = document.querySelectorAll('.allocation-bar');
    const allocationObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.width = entry.target.style.getPropertyValue('--percentage');
            }
        });
    }, { threshold: 0.5 });

    allocationBars.forEach(bar => {
        const percentage = bar.style.getPropertyValue('--percentage');
        bar.style.width = '0';
        bar.style.setProperty('--percentage', percentage);
        allocationObserver.observe(bar);
    });
});