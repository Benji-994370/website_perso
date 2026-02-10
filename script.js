// Page load transition — fade out the loading overlay once everything is ready
window.addEventListener('load', () => {
    document.body.classList.remove('loading');
    document.body.classList.add('loaded');
});

// Smooth scroll with offset for fixed header
document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const headerOffset = 100;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });

            // Close mobile nav if open
            const nav = document.getElementById('main-nav');
            const hamburger = document.querySelector('.hamburger');
            const backdrop = document.querySelector('.nav-backdrop');
            if (nav && nav.classList.contains('nav-open')) {
                nav.classList.remove('nav-open');
                hamburger.classList.remove('active');
                hamburger.setAttribute('aria-expanded', 'false');
                backdrop.classList.remove('active');
                document.body.style.overflow = '';
            }
        }
    });
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.15,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all project cards
document.querySelectorAll('.project').forEach((project) => {
    observer.observe(project);
});

// Observe testimonials
document.querySelectorAll('.testimonial').forEach((testimonial) => {
    observer.observe(testimonial);
});

// Consolidated scroll handler (parallax + header)
const header = document.querySelector('.header');
const shapes = document.querySelectorAll('.hero-bg-shape');
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
let ticking = false;

function onScroll() {
    const scrolled = window.pageYOffset;

    // Parallax effect for hero background shapes (skip if reduced motion)
    if (!prefersReducedMotion) {
        shapes.forEach((shape, index) => {
            const speed = (index + 1) * 0.3;
            shape.style.transform = `translateY(${-(scrolled * speed)}px)`;
        });
    }

    // Active navigation highlighting
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
    let currentSection = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop - 150;
        if (scrolled >= sectionTop) {
            currentSection = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentSection}`) {
            link.classList.add('active');
        }
    });

    // Show/hide scroll-to-top button
    const scrollTopBtn = document.querySelector('.scroll-to-top');
    if (scrollTopBtn) {
        scrollTopBtn.classList.toggle('visible', scrolled > 600);
    }

    // Header background change
    if (scrolled > 100) {
        header.style.background = 'rgba(15, 15, 15, 0.98)';
        header.style.backdropFilter = 'blur(10px)';
        header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.6)';
    } else {
        header.style.background = 'linear-gradient(to bottom, rgba(15, 15, 15, 1) 0%, rgba(15, 15, 15, 0.95) 70%, transparent 100%)';
        header.style.backdropFilter = 'none';
        header.style.boxShadow = 'none';
    }

    ticking = false;
}

window.addEventListener('scroll', () => {
    if (!ticking) {
        window.requestAnimationFrame(onScroll);
        ticking = true;
    }
});

// ============================================
// All DOMContentLoaded logic consolidated
// ============================================
document.addEventListener('DOMContentLoaded', function() {

    // --- Hamburger Menu ---
    const hamburger = document.querySelector('.hamburger');
    const nav = document.getElementById('main-nav');
    const backdrop = document.querySelector('.nav-backdrop');

    if (hamburger && nav) {
        hamburger.addEventListener('click', function() {
            const isOpen = nav.classList.toggle('nav-open');
            hamburger.classList.toggle('active');
            hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
            if (backdrop) backdrop.classList.toggle('active');
            document.body.style.overflow = isOpen ? 'hidden' : '';
        });

        if (backdrop) {
            backdrop.addEventListener('click', function() {
                nav.classList.remove('nav-open');
                hamburger.classList.remove('active');
                hamburger.setAttribute('aria-expanded', 'false');
                backdrop.classList.remove('active');
                document.body.style.overflow = '';
            });
        }
    }

    // --- Testimonial Carousel ---
    const carousel = document.querySelector('.testimonial-carousel');
    if (carousel) {
        const wrapper = carousel.querySelector('.testimonial-wrapper');
        const testimonials = wrapper.querySelectorAll('.testimonial');
        const prevBtn = carousel.querySelector('.carousel-prev');
        const nextBtn = carousel.querySelector('.carousel-next');
        const indicators = carousel.querySelectorAll('.indicator');

        let currentIndex = 0;
        let autoRotateInterval;
        let isPaused = false;

        function showTestimonial(index) {
            testimonials.forEach((testimonial, i) => {
                testimonial.classList.toggle('testimonial-active', i === index);
            });
            indicators.forEach((indicator, i) => {
                indicator.classList.toggle('indicator-active', i === index);
            });
            currentIndex = index;

            // Dynamically adjust wrapper height
            const activeTestimonial = testimonials[index];
            if (activeTestimonial && wrapper) {
                requestAnimationFrame(() => {
                    const testimonialHeight = activeTestimonial.offsetHeight;
                    wrapper.style.height = `${testimonialHeight + 80}px`;
                });
            }
        }

        function nextTestimonial() {
            showTestimonial((currentIndex + 1) % testimonials.length);
        }

        function prevTestimonial() {
            showTestimonial((currentIndex - 1 + testimonials.length) % testimonials.length);
        }

        function startAutoRotate() {
            if (autoRotateInterval) clearInterval(autoRotateInterval);
            autoRotateInterval = setInterval(() => {
                if (!isPaused) nextTestimonial();
            }, 15000);
        }

        function stopAutoRotate() {
            if (autoRotateInterval) {
                clearInterval(autoRotateInterval);
                autoRotateInterval = null;
            }
        }

        prevBtn.addEventListener('click', () => { prevTestimonial(); stopAutoRotate(); startAutoRotate(); });
        nextBtn.addEventListener('click', () => { nextTestimonial(); stopAutoRotate(); startAutoRotate(); });

        indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => { showTestimonial(index); stopAutoRotate(); startAutoRotate(); });
        });

        // Keyboard navigation for carousel
        carousel.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') { prevTestimonial(); stopAutoRotate(); startAutoRotate(); }
            if (e.key === 'ArrowRight') { nextTestimonial(); stopAutoRotate(); startAutoRotate(); }
        });

        testimonials.forEach((testimonial) => {
            testimonial.addEventListener('mouseenter', () => { isPaused = true; });
            testimonial.addEventListener('mouseleave', () => { isPaused = false; });
        });

        showTestimonial(0);
        startAutoRotate();
    }

    // --- Services Modal ---
    const modal = document.querySelector('.modal-overlay');
    const modalTriggers = document.querySelectorAll('.service-cta, .consultation-trigger');
    const modalClose = document.querySelector('.modal-close');

    if (modal) {
        modalTriggers.forEach(trigger => {
            trigger.addEventListener('click', function(e) {
                const href = trigger.getAttribute('href');
                if (!href || href === '#') {
                    e.preventDefault();
                    modal.classList.add('active');
                    document.body.style.overflow = 'hidden';
                }
            });
        });

        if (modalClose) {
            modalClose.addEventListener('click', function() {
                modal.classList.remove('active');
                document.body.style.overflow = '';
            });
        }

        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                modal.classList.remove('active');
                document.body.style.overflow = '';
            }
        });

        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && modal.classList.contains('active')) {
                modal.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }

    // --- Stat Counter Animation ---
    // Numbers count up when scrolled into view (uses Intersection Observer like the rest of the site)
    const statNumbers = document.querySelectorAll('.hero-stat-number[data-count]');
    if (statNumbers.length > 0) {
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    const target = parseInt(el.dataset.count);
                    const suffix = el.dataset.suffix || '';
                    let current = 0;
                    const duration = 1500; // 1.5 seconds
                    const steps = duration / 16; // ~60fps
                    const increment = Math.max(1, Math.ceil(target / steps));

                    function count() {
                        current += increment;
                        if (current >= target) {
                            el.textContent = target + suffix;
                        } else {
                            el.textContent = current + suffix;
                            requestAnimationFrame(count);
                        }
                    }
                    requestAnimationFrame(count);
                    statsObserver.unobserve(el);
                }
            });
        }, { threshold: 0.5 });

        statNumbers.forEach(el => statsObserver.observe(el));
    }

    // --- Scroll-to-Top Button ---
    const scrollTopBtn = document.querySelector('.scroll-to-top');
    if (scrollTopBtn) {
        scrollTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // --- Touch/Swipe Support for Testimonial Carousel ---
    // Swipe left/right to navigate testimonials on mobile
    const carouselForSwipe = document.querySelector('.testimonial-wrapper');
    if (carouselForSwipe) {
        let touchStartX = 0;
        let touchEndX = 0;
        const swipeThreshold = 50;

        carouselForSwipe.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });

        carouselForSwipe.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].screenX;
            const diff = touchStartX - touchEndX;
            if (Math.abs(diff) > swipeThreshold) {
                // Access carousel functions via buttons (they're in the same scope)
                const nextBtn = document.querySelector('.carousel-next');
                const prevBtn = document.querySelector('.carousel-prev');
                if (diff > 0 && nextBtn) {
                    nextBtn.click();
                } else if (diff < 0 && prevBtn) {
                    prevBtn.click();
                }
            }
        });
    }

}); // end DOMContentLoaded
