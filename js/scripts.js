/*!
* Khalida Educational Foundation
* Enhanced JavaScript for Interactive Features
*/
window.addEventListener('DOMContentLoaded', event => {

    let scrollToTopVisible = false;
    const navbar = document.getElementById('mainNav');
    
    // Enhanced Navbar scroll effect with smooth transition
    function navbarScrollEffect() {
        if (window.scrollY > 100) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    }
    
    // Call on load and scroll
    navbarScrollEffect();
    window.addEventListener('scroll', navbarScrollEffect, { passive: true });

    // Enhanced mobile menu handling with better UX
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    
    // Close responsive navbar when link is clicked (improved)
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            // Don't close if it's a dropdown toggle
            if (!this.classList.contains('dropdown-toggle') && navbarCollapse.classList.contains('show')) {
                navbarToggler.click();
            }
        });
    });

    // Handle dropdown menus on mobile/tablet
    if (window.innerWidth < 992) {
        dropdownToggles.forEach(toggle => {
            toggle.addEventListener('click', function(e) {
                e.preventDefault();
                const dropdown = this.nextElementSibling;
                
                // Close other dropdowns
                document.querySelectorAll('.dropdown-menu').forEach(menu => {
                    if (menu !== dropdown) {
                        menu.style.display = 'none';
                    }
                });
                
                // Toggle current dropdown
                if (dropdown.style.display === 'block') {
                    dropdown.style.display = 'none';
                } else {
                    dropdown.style.display = 'block';
                }
            });
        });
    }

    // Responsive navbar resize handler
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            if (window.innerWidth >= 992) {
                // Remove inline styles on desktop
                document.querySelectorAll('.dropdown-menu').forEach(menu => {
                    menu.style.display = '';
                });
            }
        }, 250);
    });

    // Add active class to current page nav item
    const currentLocation = location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        let href = link.getAttribute('href');
        if (currentLocation.includes(href) && href !== '/' && href !== 'index.html') {
            link.classList.add('active');
            // Also mark parent dropdown as active if applicable
            const parentDropdown = link.closest('.dropdown');
            if (parentDropdown) {
                parentDropdown.querySelector('.dropdown-toggle').classList.add('active');
            }
        }
    });

    // Scroll to top button appear
    document.addEventListener('scroll', () => {
        const scrollToTop = document.body.querySelector('.scroll-to-top');
        // Only proceed if scroll-to-top element exists
        if (!scrollToTop) return;
        
        if (document.documentElement.scrollTop > 100) {
            if (!scrollToTopVisible) {
                fadeIn(scrollToTop);
                scrollToTopVisible = true;
            }
        } else {
            if (scrollToTopVisible) {
                fadeOut(scrollToTop);
                scrollToTopVisible = false;
            }
        }
    }, { passive: true })

    function fadeOut(el) {
        if (!el) return;
        el.style.opacity = 1;
        (function fade() {
            if ((el.style.opacity -= .1) < 0) {
                el.style.display = "none";
            } else {
                requestAnimationFrame(fade);
            }
        })();
    };

    function fadeIn(el, display) {
        if (!el) return;
        el.style.opacity = 0;
        el.style.display = display || "block";
        (function fade() {
            var val = parseFloat(el.style.opacity);
            if (!((val += .1) > 1)) {
                el.style.opacity = val;
                requestAnimationFrame(fade);
            }
        })();
    };

    // ===== ENHANCED FEATURES =====
    
    // Impact Statistics Counter Animation
    function animateCounter(element) {
        const target = parseInt(element.getAttribute('data-target'));
        const duration = 2000; // 2 seconds
        const increment = target / (duration / 16); // 60fps
        let current = 0;
        
        const updateCounter = () => {
            current += increment;
            if (current < target) {
                element.textContent = Math.ceil(current).toLocaleString();
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target.toLocaleString();
            }
        };
        
        updateCounter();
    }
    
    // Trigger counter animation when section is visible
    const observerOptions = {
        threshold: 0.5
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counters = entry.target.querySelectorAll('.stat-number');
                counters.forEach(counter => {
                    if (counter.textContent === '0') {
                        animateCounter(counter);
                    }
                });
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    const impactSection = document.querySelector('#impact');
    if (impactSection) {
        observer.observe(impactSection);
    }
    
    // Gallery Modal Functionality
    const galleryModal = document.getElementById('galleryModal');
    if (galleryModal) {
        galleryModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;
            const imgSrc = button.getAttribute('data-img');
            const imgTitle = button.getAttribute('data-title');
            
            const modalImage = galleryModal.querySelector('#galleryModalImage');
            const modalTitle = galleryModal.querySelector('#galleryModalLabel');
            
            modalImage.src = imgSrc;
            modalImage.alt = imgTitle;
            modalTitle.textContent = imgTitle;
        });
    }
    
    // Contact Form Submission (handled via formsubmit.co action)
    // No JS interception needed so the form posts directly and delivers email from static hosting
    
    // Newsletter Form Submission
    const newsletterForms = document.querySelectorAll('.newsletter-form');
    newsletterForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = form.querySelector('input[type="email"]').value;
            
            // Here you would typically send to a newsletter service
            alert('Thank you for subscribing! You will receive updates at: ' + email);
            form.reset();
        });
    });
    
    // Smooth Scroll for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '#!') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    // Active Navigation State
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (pageYOffset >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href && (href === '#' + current || href.includes('#' + current))) {
                link.classList.add('active');
            }
        });
    });
    
    // Add fade-in animation to elements as they come into view
    const fadeElements = document.querySelectorAll('.program-card, .testimonial-card, .benefit-card');
    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                fadeObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    fadeElements.forEach(element => {
        fadeObserver.observe(element);
    });

});
