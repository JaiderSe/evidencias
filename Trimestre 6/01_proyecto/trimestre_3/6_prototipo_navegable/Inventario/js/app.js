document.addEventListener('DOMContentLoaded', function() {
    // Elementos del DOM
    const productForm = document.getElementById('productForm');
    const productTableBody = document.getElementById('productTableBody');
    const submitBtn = document.getElementById('submitBtn');
    const cancelBtn = document.getElementById('cancelBtn');
    
    // Variables de estado
    let editingId = null;
    
    // Cargar productos al iniciar
    loadProducts();
    
    // Evento para enviar el formulario
    productForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const product = {
            id: editingId || Date.now().toString(),
            name: document.getElementById('productName').value,
            price: parseFloat(document.getElementById('productPrice').value),
            stock: parseInt(document.getElementById('productStock').value)
        };
        
        saveProduct(product);
        productForm.reset();
        editingId = null;
        submitBtn.textContent = 'Guardar';
        cancelBtn.style.display = 'none';
    });
    
    // Evento para cancelar edición
    cancelBtn.addEventListener('click', function() {
        productForm.reset();
        editingId = null;
        submitBtn.textContent = 'Guardar';
        cancelBtn.style.display = 'none';
    });
    
    // Función para cargar productos
    function loadProducts() {
        const products = getProducts();
        productTableBody.innerHTML = '';
        
        products.forEach(product => {
            const row = document.createElement('tr');
            
            row.innerHTML = `
                <td>${product.name}</td>
                <td>$${product.price.toFixed(2)}</td>
                <td>${product.stock}</td>
                <td>
                    <button class="action-btn edit-btn" data-id="${product.id}">Editar</button>
                    <button class="action-btn delete-btn" data-id="${product.id}">Eliminar</button>
                </td>
            `;
            
            productTableBody.appendChild(row);
        });
        
        // Agregar eventos a los botones de editar y eliminar
        document.querySelectorAll('.edit-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                editProduct(this.getAttribute('data-id'));
            });
        });
        
        document.querySelectorAll('.delete-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                deleteProduct(this.getAttribute('data-id'));
            });
        });
    }
    
    // Función para obtener todos los productos
    function getProducts() {
        const products = localStorage.getItem('products');
        return products ? JSON.parse(products) : [];
    }
    
    // Función para guardar un producto (Create/Update)
    function saveProduct(product) {
        let products = getProducts();
        
        if (editingId) {
            // Actualizar producto existente
            products = products.map(p => p.id === product.id ? product : p);
        } else {
            // Agregar nuevo producto
            products.push(product);
        }
        
        localStorage.setItem('products', JSON.stringify(products));
        loadProducts();
    }
    
    // Función para editar un producto (Read)
    function editProduct(id) {
        const products = getProducts();
        const product = products.find(p => p.id === id);
        
        if (product) {
            document.getElementById('productId').value = product.id;
            document.getElementById('productName').value = product.name;
            document.getElementById('productPrice').value = product.price;
            document.getElementById('productStock').value = product.stock;
            
            editingId = product.id;
            submitBtn.textContent = 'Actualizar';
            cancelBtn.style.display = 'inline-block';
        }
    }
    
    // Función para eliminar un producto (Delete)
    function deleteProduct(id) {
        if (confirm('¿Estás seguro de eliminar este producto?')) {
            let products = getProducts();
            products = products.filter(p => p.id !== id);
            
            localStorage.setItem('products', JSON.stringify(products));
            loadProducts();
            
            // Si estábamos editando el producto eliminado, cancelar edición
            if (editingId === id) {
                productForm.reset();
                editingId = null;
                submitBtn.textContent = 'Guardar';
                cancelBtn.style.display = 'none';
            }
        }
    }
});
