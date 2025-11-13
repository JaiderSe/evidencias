app/
│
├── __init__.py
├── config.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── categoria.py
│   ├── ingrediente.py
│   ├── platillo.py
│   ├── mesa.py
│   ├── cliente.py
│   ├── pedido.py
│   ├── detalle_pedido.py
│   └── inventario.py
│
├── controllers/
│   ├── __init__.py
│   ├── auth_controller.py
│   ├── admin_controller.py
│   ├── chef_controller.py
│   ├── mesero_controller.py
│   ├── inventario_controller.py
│   ├── menu_controller.py
│   ├── pedidos_controller.py
│   └── mesas_controller.py
│
├── templates/
│   ├── base.html
│   │
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   │
│   ├── admin/
│   │   ├── dashboard.html
│   │   ├── usuarios/
│   │   │   ├── list.html
│   │   │   └── form.html
│   │   └── reportes/
│   │       └── ventas.html
│   │
│   ├── chef/
│   │   ├── dashboard.html
│   │   ├── ordenes.html
│   │   └── recetas/
│   │       ├── list.html
│   │       └── form.html
│   │
│   ├── mesero/
│   │   ├── dashboard.html
│   │   ├── mesas/
│   │   │   ├── list.html
│   │   │   └── detalles.html
│   │   └── pedidos/
│   │       ├── nuevo.html
│   │       └── list.html
│   │
│   ├── inventario/
│   │   ├── dashboard.html
│   │   ├── ingredientes/
│   │   │   ├── list.html
│   │   │   └── form.html
│   │   └── movimientos.html
│   │
│   └── shared/
│       ├── menu.html
│       └── platillos/
│           ├── card.html
│           └── detalles.html
│
└── static/
    ├── css/
    │   └── styles.css
    ├── js/
    │   └── scripts.js
    └── img/
        └── logo.png