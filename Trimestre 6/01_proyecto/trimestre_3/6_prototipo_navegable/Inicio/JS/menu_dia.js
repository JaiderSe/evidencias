// Seleccionamos los botones
const filtroBebidas = document.getElementById('filtro-bebidas');
const filtroPlatoFuerte = document.getElementById('filtro-plato-fuerte');
const filtroEntradas = document.getElementById('filtro-entradas');
const filtroPostres = document.getElementById('filtro-postres');
const filtroTodo = document.getElementById('filtro-todo'); // Nuevo botón "Mostrar Todo"

// Seleccionamos todos los elementos de las tarjetas de platos
const platos = document.querySelectorAll('.plato-card');

// Función para mostrar todos los platos
function mostrarTodos() {
  platos.forEach(plato => {
    plato.style.display = 'block'; // Muestra todos los platos
  });
}

// Función para filtrar por categoría
function filtrarPorCategoria(categoria) {
  platos.forEach(plato => {
    if (plato.classList.contains(categoria)) {
      plato.style.display = 'block'; // Muestra el plato si pertenece a la categoría
    } else {
      plato.style.display = 'none'; // Oculta el plato si no pertenece a la categoría
    }
  });
}

// Obtener todos los botones de filtro en un array
const botonesFiltro = document.querySelectorAll('button');

// Función para resaltar el botón activo
function resaltarBotonActivo(botonSeleccionado) {
  botonesFiltro.forEach(boton => {
    boton.classList.remove('activo');
  });
  botonSeleccionado.classList.add('activo');
}

// Eventos para los botones
filtroBebidas.addEventListener('click', (e) => {
    filtrarPorCategoria('bebida');
    resaltarBotonActivo(e.target);
  });
  
  filtroEntradas.addEventListener('click', (e) => {
    filtrarPorCategoria('entrada');
    resaltarBotonActivo(e.target);
  });
  
  filtroPostres.addEventListener('click', (e) => {
    filtrarPorCategoria('postre');
    resaltarBotonActivo(e.target);
  });
  
  filtroTodo.addEventListener('click', (e) => {
    mostrarTodos();
    resaltarBotonActivo(e.target);
  });
  
  filtroPlatoFuerte.addEventListener('click', (e) => {
    filtrarPorCategoria('plato-fuerte');
    resaltarBotonActivo(e.target);
  });
  

// Mostrar todos los elementos al cargar la página
mostrarTodos();
