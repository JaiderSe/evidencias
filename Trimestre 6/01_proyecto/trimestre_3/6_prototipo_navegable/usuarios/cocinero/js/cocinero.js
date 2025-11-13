const tableBody = document.querySelector(".order-table tbody");
let pedidos = JSON.parse(localStorage.getItem("pedidos")) || [];

function estadoTexto(estado) {
    switch (estado) {
        case 'pending': return 'Pendiente';
        case 'preparing': return 'En preparación';
        case 'ready': return 'Listo';
        default: return estado;
    }
}

function renderPedidos(filtro = 'all') {
    tableBody.innerHTML = "";
    pedidos.forEach(pedido => {
        if (filtro === 'all' || pedido.estado === filtro) {
            const fila = document.createElement("tr");
            fila.className = `status-${pedido.estado} priority-high`;

            let botonHTML = "";
            if (pedido.estado === "pending") {
                botonHTML = `<button class="btn btn-estado" data-id="${pedido.id}">Preparar</button>`;
            } else if (pedido.estado === "preparing") {
                botonHTML = `<button class="btn btn-estado" data-id="${pedido.id}">Marcar como Listo</button>`;
            }

            fila.innerHTML = `
                <td class="order-id">${pedido.id}</td>
                <td>${pedido.cliente}</td>
                <td>${pedido.mesa}</td>
                <td>${pedido.items}</td>
                <td>${estadoTexto(pedido.estado)}</td>
                <td class="timestamp">${pedido.hora}</td>
                <td>${botonHTML}</td>
            `;

            tableBody.appendChild(fila);
        }
    });
}

// Cambiar estado del pedido (solo cocinero)
tableBody.addEventListener("click", e => {
    if (e.target.classList.contains("btn-estado")) {
        const id = e.target.getAttribute("data-id");
        const pedido = pedidos.find(p => p.id === id);

        if (pedido.estado === "pending") {
            pedido.estado = "preparing";
        } else if (pedido.estado === "preparing") {
            pedido.estado = "ready";
        }

        localStorage.setItem("pedidos", JSON.stringify(pedidos));
        const filtroActual = document.querySelector(".filter-btn.active")?.getAttribute("data-filter") || "all";
        renderPedidos(filtroActual);
    }
});

// Filtro por estado
document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        renderPedidos(btn.getAttribute('data-filter'));
    });
});

// Logout
document.getElementById('logoutBtn').addEventListener('click', function () {
    localStorage.removeItem('currentUser');
    window.location.href = '../Inicio/index.html';
});

// Inicializar tabla
renderPedidos();
