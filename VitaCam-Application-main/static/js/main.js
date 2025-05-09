// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    const menuBtn = document.querySelector('.fa-bars');
    const navbar = document.querySelector('.navbar');
    const header = document.querySelector('header');

    // Toggle mobile menu
    menuBtn.addEventListener('click', () => {
        menuBtn.classList.toggle('fa-times');
        navbar.classList.toggle('active');
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!navbar.contains(e.target) && !menuBtn.contains(e.target)) {
            menuBtn.classList.remove('fa-times');
            navbar.classList.remove('active');
        }
    });

    // Header scroll effect
    window.addEventListener('scroll', () => {
        if (window.scrollY > 30) {
            header.classList.add('header-active');
        } else {
            header.classList.remove('header-active');
        }
    });

    // File upload preview
    const fileInput = document.querySelector('input[type="file"]');
    const uploadLabel = document.querySelector('.upload-label');
    const uploadIcon = document.querySelector('.upload-label i');
    const uploadText = document.querySelector('.upload-label span');

    if (fileInput) {
        fileInput.addEventListener('change', function() {
            if (this.files && this.files[0]) {
                const fileName = this.files[0].name;
                uploadText.textContent = fileName;
                uploadIcon.classList.remove('fa-cloud-upload-alt');
                uploadIcon.classList.add('fa-check');
                uploadLabel.style.borderColor = 'var(--primary-color)';
            }
        });
    }

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
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

    // Animation on scroll
    const animateOnScroll = () => {
        const elements = document.querySelectorAll('.info-box, .result-container');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.3;

            if (elementPosition < screenPosition) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };

    // Set initial styles for animation
    document.querySelectorAll('.info-box, .result-container').forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'all 0.5s ease';
    });

    // Run animation on scroll
    window.addEventListener('scroll', animateOnScroll);
    // Run once on page load
    animateOnScroll();
}); 