// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Elemento del botón
    const themeToggle = document.getElementById('themeToggle');
    
    // 1. Cargar tema guardado o usar light por defecto
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.className = savedTheme;
    
    // 2. Función para alternar tema
    function toggleTheme() {
        const newTheme = document.body.className === 'dark' ? 'light' : 'dark';
        document.body.className = newTheme;
        localStorage.setItem('theme', newTheme);
        
        // Opcional: Mostrar en consola para depuración
        console.log('Tema cambiado a:', newTheme);
    }
    
    // 3. Asignar evento
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    } else {
        console.error('No se encontró el botón themeToggle');
    }
    
    // Opcional: Mostrar estado inicial
    console.log('Tema inicial:', savedTheme);
})