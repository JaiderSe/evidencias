// === mesero.js ===
let pedidos = JSON.parse(localStorage.getItem('pedidos')) || [];

const orderForm = document.getElementById("orderForm");
const tableBody = document.querySelector(".order-table tbody");

const generarID = () => "#" + String(pedidos.length + 1).padStart(3, '0');

function renderPedidos(filtro = 'all') {
    tableBody.innerHTML = "";
    pedidos.forEach(pedido => {
        if (filtro === 'all' || pedido.estado === filtro) {
            const fila = document.createElement("tr");
            fila.className = `status-${pedido.estado} priority-${pedido.prioridad}`;

            const puedeServir = pedido.estado === 'ready';
            const botonServir = `<button class="btn btn-estado" data-id="${pedido.id}" ${!puedeServir ? 'disabled' : ''}>Servir</button>`;

            fila.innerHTML = `
                <td class="order-id">${pedido.id}</td>
                <td>${pedido.cliente}</td>
                <td>${pedido.mesa}</td>
                <td>${pedido.items}</td>
                <td>${estadoTexto(pedido.estado)}</td>
                <td class="timestamp">${pedido.hora}</td>
                <td>${botonServir}</td>
            `;

            tableBody.appendChild(fila);
        }
    });
}

function estadoTexto(estado) {
    switch (estado) {
        case 'pending': return 'Pendiente';
        case 'preparing': return 'En preparación';
        case 'ready': return 'Listo';
        default: return estado;
    }
}

orderForm.addEventListener("submit", e => {
    e.preventDefault();

    const cliente = document.getElementById("customer").value.trim();
    const items = document.getElementById("items").value.trim();
    const mesa = document.getElementById("mesa").value;

    if (!cliente || !items || mesa === "default") {
        alert("Por favor completa todos los campos");
        return;
    }

    const nuevoPedido = {
        id: generarID(),
        cliente,
        items,
        mesa,
        estado: "pending",
        prioridad: "high",
        hora: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    pedidos.push(nuevoPedido);
    localStorage.setItem("pedidos", JSON.stringify(pedidos));
    renderPedidos();

    orderForm.reset();
});

// Acción del mesero: solo puede "entregar" si el pedido está listo
// (aquí podemos simular "entregado" eliminándolo de la tabla o actualizando estado si quieres)
tableBody.addEventListener("click", e => {
    if (e.target.classList.contains("btn-estado")) {
        const id = e.target.getAttribute("data-id");
        const pedido = pedidos.find(p => p.id === id);

        if (pedido.estado === "ready") {
            alert(`Pedido ${id} entregado al cliente.`);
            // Puedes eliminarlo o marcarlo como "entregado" si gustas
            // Ejemplo: pedido.estado = "entregado";
            // Aquí lo eliminamos:
            pedidos = pedidos.filter(p => p.id !== id);
            localStorage.setItem("pedidos", JSON.stringify(pedidos));
            renderPedidos(document.querySelector(".filter-btn.active").getAttribute("data-filter"));
        }
    }
});

document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filtro = btn.getAttribute('data-filter');
        renderPedidos(filtro);
    });
});

renderPedidos();