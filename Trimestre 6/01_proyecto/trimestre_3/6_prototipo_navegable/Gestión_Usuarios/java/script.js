let usuarios = [
  { id: 1, nombre: "Ana Torres", correo: "ana@ejemplo.com", contraseña: "1234", fecha: "2025-04-01", rol: "Admin" },
  { id: 2, nombre: "Carlos Ruiz", correo: "carlos@ejemplo.com", contraseña: "abcd", fecha: "2025-04-02", rol: "Mesero" },
  { id: 3, nombre: "Laura Gómez", correo: "laura@ejemplo.com", contraseña: "laura123", fecha: "2025-04-10", rol: "Cliente" },
  { id: 4, nombre: "Pedro Martínez", correo: "pedro@ejemplo.com", contraseña: "pedro456", fecha: "2025-04-15", rol: "Cocinero" }
];

let idActual = usuarios.length;

function mostrarUsuarios() {
  const tbody = document.querySelector("#tablaUsuarios tbody");
  tbody.innerHTML = "";

  usuarios.forEach((usuario, index) => {
    const fila = document.createElement("tr");
    fila.innerHTML = `
      <td>${usuario.id}</td>
      <td contenteditable="false">${usuario.nombre}</td>
      <td contenteditable="false">${usuario.correo}</td>
      <td contenteditable="false">${usuario.contraseña}</td>
      <td contenteditable="false">${usuario.fecha}</td>
      <td contenteditable="false">${usuario.rol}</td>
      <td>
        <button class="editar">Editar</button>
        <button class="guardar" style="display:none">Guardar</button>
        <button class="cancelar" style="display:none">Cancelar</button>
        <button class="eliminar">Eliminar</button>
      </td>
    `;
    tbody.appendChild(fila);

    const editarBtn = fila.querySelector(".editar");
    const guardarBtn = fila.querySelector(".guardar");
    const cancelarBtn = fila.querySelector(".cancelar");
    const eliminarBtn = fila.querySelector(".eliminar");
    const celdas = fila.querySelectorAll("td[contenteditable]");

    editarBtn.addEventListener("click", () => {
      celdas.forEach(celda => celda.contentEditable = "true");
      editarBtn.style.display = "none";
      guardarBtn.style.display = "inline";
      cancelarBtn.style.display = "inline";
      eliminarBtn.style.display = "none";
    });

    cancelarBtn.addEventListener("click", () => {
      mostrarUsuarios();
    });

    guardarBtn.addEventListener("click", () => {
      const nuevosValores = Array.from(celdas).map(c => c.innerText.trim());
      usuarios[index] = {
        id: usuario.id,
        nombre: nuevosValores[0],
        correo: nuevosValores[1],
        contraseña: nuevosValores[2],
        fecha: nuevosValores[3],
        rol: nuevosValores[4]
      };
      mostrarUsuarios();
    });

    eliminarBtn.addEventListener("click", () => {
      usuarios.splice(index, 1);
      mostrarUsuarios();
    });
  });
}

document.getElementById("buscador").addEventListener("input", function () {
  const filtro = this.value.toLowerCase();
  const filas = document.querySelectorAll("#tablaUsuarios tbody tr");

  filas.forEach(fila => {
    const texto = fila.innerText.toLowerCase();
    fila.style.display = texto.includes(filtro) ? "" : "none";
  });
});

mostrarUsuarios();
