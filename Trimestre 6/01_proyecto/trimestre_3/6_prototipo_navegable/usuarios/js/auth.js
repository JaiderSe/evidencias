
/**
 * Verifica si hay un usuario autenticado
 * Redirige a la página correspondiente según su rol
 */
function checkAuth() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    const currentPage = window.location.pathname;
    
    // Páginas que no requieren autenticación
    const publicPages = ['/index.html', '/login.html', '/register.html'];
    
    // Si no está en una página pública y no hay usuario, redirigir a login
    if (!publicPages.some(page => currentPage.endsWith(page)) && !currentUser) {
        window.location.href = 'login.html';
        return;
    }
    
    // Si está logueado pero intenta acceder a login/register, redirigir según rol
    if (currentUser && (currentPage.endsWith('login.html') || currentPage.endsWith('register.html'))) {
        redirectByRole(currentUser.role);
    }
    
    // Verificar acceso a rutas según rol
    if (currentUser) {
        const isAdminPage = currentPage.includes('/admin/');
        const isClientPage = currentPage.includes('/cliente/');
        
        if (isAdminPage && currentUser.role !== 'admin') {
            window.location.href = '../cliente/productos.html';
        }
        
        if (isClientPage && currentUser.role !== 'cliente') {
            window.location.href = '../admin/dashboard.html';
        }
    }
}

/**
 * Redirige al usuario según su rol
 * @param {string} role - Rol del usuario (admin/cliente)
 */
function redirectByRole(role) {
    if (role === 'admin') {
        window.location.href = 'admin/index.html';
    } 
    else if (role === 'cliente') {
        window.location.href = '../../Inicio/index.html';
    }
    else if (role === 'cocinero') {
        window.location.href = 'cocinero/index.html';
    }
    else if (role === 'mesero') {
        window.location.href = '../../Pedidos/index.html';
    }
    else {
        window.location.href = '../../Inicio/index.html';
    }
}

// Ejecutar verificación al cargar la página
document.addEventListener('DOMContentLoaded', checkAuth);