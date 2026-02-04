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

// Custom cursor removed for performance

// Add stagger animation to project cards
const projects = document.querySelectorAll('.project');
projects.forEach((project, index) => {
    project.style.transitionDelay = `${index * 0.15}s`;
});

// Preload critical fonts
const preloadFonts = () => {
    const fonts = [
        new FontFace('Cormorant Garamond', 'url(https://fonts.gstatic.com/s/cormorantgaramond/v16/co3bmX5slCNuHLi8bLeY9MK7whWMhyjQAllvuQWJ5heb_w.woff2)'),
        new FontFace('Work Sans', 'url(https://fonts.gstatic.com/s/worksans/v18/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K0nWNigDp6_cOyA.woff2)')
    ];

    fonts.forEach(font => {
        font.load().then(loadedFont => {
            document.fonts.add(loadedFont);
        });
    });
};

preloadFonts();

// Testimonial Carousel with Auto-rotation
const initTestimonialCarousel = () => {
    const carousel = document.querySelector('.testimonial-carousel');
    if (!carousel) return;

    const wrapper = carousel.querySelector('.testimonial-wrapper');
    const testimonials = wrapper.querySelectorAll('.testimonial');
    const prevBtn = carousel.querySelector('.carousel-prev');
    const nextBtn = carousel.querySelector('.carousel-next');
    const indicators = carousel.querySelectorAll('.indicator');

    let currentIndex = 0;
    let autoRotateInterval;
    let isPaused = false;

    // Show testimonial by index
    function showTestimonial(index) {
        testimonials.forEach((testimonial, i) => {
            testimonial.classList.toggle('testimonial-active', i === index);
        });
        indicators.forEach((indicator, i) => {
            indicator.classList.toggle('indicator-active', i === index);
        });
        currentIndex = index;
    }

    // Go to next testimonial
    function nextTestimonial() {
        const next = (currentIndex + 1) % testimonials.length;
        showTestimonial(next);
    }

    // Go to previous testimonial
    function prevTestimonial() {
        const prev = (currentIndex - 1 + testimonials.length) % testimonials.length;
        showTestimonial(prev);
    }

    // Start auto-rotation
    function startAutoRotate() {
        if (autoRotateInterval) clearInterval(autoRotateInterval);
        autoRotateInterval = setInterval(() => {
            if (!isPaused) {
                nextTestimonial();
            }
        }, 15000); // 15 seconds
    }

    // Stop auto-rotation
    function stopAutoRotate() {
        if (autoRotateInterval) {
            clearInterval(autoRotateInterval);
            autoRotateInterval = null;
        }
    }

    // Event listeners for controls
    prevBtn.addEventListener('click', () => {
        prevTestimonial();
        stopAutoRotate();
        startAutoRotate();
    });

    nextBtn.addEventListener('click', () => {
        nextTestimonial();
        stopAutoRotate();
        startAutoRotate();
    });

    // Event listeners for indicators
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            showTestimonial(index);
            stopAutoRotate();
            startAutoRotate();
        });
    });

    // Pause on hover over any testimonial
    testimonials.forEach((testimonial) => {
        testimonial.addEventListener('mouseenter', () => {
            isPaused = true;
        });

        testimonial.addEventListener('mouseleave', () => {
            isPaused = false;
        });
    });

    // Initialize
    showTestimonial(0);
    startAutoRotate();
};

document.addEventListener('DOMContentLoaded', initTestimonialCarousel);
