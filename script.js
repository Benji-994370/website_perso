// Smooth scroll with offset for fixed header
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
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
let ticking = false;

function onScroll() {
    const scrolled = window.pageYOffset;

    // Parallax effect for hero background shapes
    shapes.forEach((shape, index) => {
        const speed = (index + 1) * 0.3;
        shape.style.transform = `translateY(${-(scrolled * speed)}px)`;
    });

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
    const modalTriggers = document.querySelectorAll('.service-cta');
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

}); // end DOMContentLoaded
