// Slider functionality
document.addEventListener('DOMContentLoaded', function() {
    // Slider
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    let currentSlide = 0;
    
    function showSlide(n) {
        slides.forEach(slide => slide.classList.remove('active'));
        slides[n].classList.add('active');
        currentSlide = n;
    }
    
    function nextSlide() {
        let newIndex = (currentSlide + 1) % slides.length;
        showSlide(newIndex);
    }
    
    function prevSlide() {
        let newIndex = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(newIndex);
    }
    
    if (nextBtn && prevBtn) {
        nextBtn.addEventListener('click', nextSlide);
        prevBtn.addEventListener('click', prevSlide);
        
        // Auto slide
        setInterval(nextSlide, 5000);
    }
    
    // Check if user is logged in and redirect if trying to access protected pages
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    const protectedPages = ['indexusuario.html', 'perfil.html'];
    const currentPage = window.location.pathname.split('/').pop();
    
    if (protectedPages.includes(currentPage)) {
        if (!currentUser) {
            window.location.href = 'index.html';
        }
    }
    
    // If user is logged in and tries to access login/register, redirect to user home
    if (currentUser && (currentPage === 'login.html' || currentPage === 'register.html')) {
        window.location.href = 'indexusuario.html';
    }
});
