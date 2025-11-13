## 🚀 RestauSync
![alt text](fondo.png) 


## 📜 Descripción
Repositorio para un proyecto sobre un aplicativo para Restaurantes

"Bienvenido a RestauSync, donde la tradición y la innovación se unen en un viaje gastronómico único. Disfruta de nuestra especialidad, la Arepa RestauSync de la Casa, y explora nuestra variedad de platos colombianos incluyendo la famosa Bandeja Paisa. ¡Ven y descubre el sabor de la autenticidad en un ambiente acogedor y elegante!"

## 🛠️ Tecnologías

- **Larabel**: Framework Backend.
- **Angular**: Framework Frontend.
- **Xampp**: Gestor de bases de datos de código abierto.
- **HTML**: Lenguaje de etiquetado para la representación de la página.



## 📁 Estructura del Proyecto

 ```text
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
   ```
**🖥 Página Web:** 
[Link](https://drive.google.com/drive/folders/1sXHN52Wap0UovdsT4diPcBXqt-dIDT79?usp=sharing)

**📊 Mapa de Navegación del sistema:**
[Link](https://drive.google.com/file/d/1xrKbX342PzqKwv00y0xOOYbQdXqd4mg5/view?usp=sharing)

**📃 Documento:**
[link](https://docs.google.com/document/d/15r4De55eXJv-mmLM6LAxWpgDSMNhAgRu/edit?usp=drivesdk&ouid=108198849053322034172&rtpof=true&sd=true)

**📃 Diseño UX/UI:**
[link](https://docs.google.com/document/d/1uYjzObtSr7cGoRIv3svmb5KaIqbRuRQ-yJIf0PurmhI/edit?usp=sharing)

**📊 Presentación trimestre 2:**
[Link](https://docs.google.com/presentation/d/1oB6k4QIMxJEdAeV6bUasqtCnlSp9KzXe/edit?usp=sharing&ouid=104681654974810316499&rtpof=true&sd=true)

**📊 Presentación trimestre 3:**
[Link](https://docs.google.com/presentation/d/1YPNXa6ZauhpDQq5R15n4pxE0JnbpGSFp/edit?usp=sharing&ouid=104681654974810316499&rtpof=true&sd=true)

**📊 Presentación trimestre 4:**
[Link](https://docs.google.com/presentation/d/1nVMbFrQCrTj2hJvOb4ORm9j0vUUVpJdD/edit?slide=id.p1#slide=id.p1)

**📊 Presentación trimestre 5:**
[Link](https://docs.google.com/presentation/d/1cb3NGtYcfXdklR3_MDdDhfMQn4S4nEf2/edit?usp=sharing&ouid=116668543162587748605&rtpof=true&sd=true)

**📊 Presentación trimestre 6:**
[Link](https://docs.google.com/presentation/d/1cb3NGtYcfXdklR3_MDdDhfMQn4S4nEf2/edit?usp=sharing&ouid=116668543162587748605&rtpof=true&sd=true)



**🚀 Mockup:**
https://drive.google.com/file/d/1RRVvbDGRa0bgOkOfDM5DY045C1C7dRuq/view?usp=sharing




## Compilar el Código

Para ejecutar la página web que utiliza HTML, MySQL y Flask:

1. **Clona el repositorio** :

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_PROYECTO>
    ```

2. **Instala las dependencias de Python** tener `pip` y un entorno virtual:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Configura la base de datos MySQL**:

    - Asegúrate de tener MySQL instalado y en ejecución.
    - Crea una base de datos y un usuario para la aplicación.
    - Actualiza las credenciales de conexión en el archivo de configuración (`config.py` o `.env`).

4. **Inicializa la base de datos** (si es necesario):

    ```bash
    # Ejecuta el script de migración o inicialización según la estructura del proyecto
    python scripts/init_db.py
    ```

5. **Ejecuta las aplicaciones backend y frontend**:

    ```bash
    npm start
    ```

6. **Abre la aplicación en tu navegador**:

    Normalmente estará disponible en [http://localhost:5000](http://localhost:5000).

> **Nota:** Si usas XAMPP para gestionar MySQL, asegúrate de que el servicio de MySQL esté iniciado antes de correr la aplicación.



## 🖥️ Ejecutar la Aplicación

## 👥 Participantes


JAIDER SEBASTIAN MORENO QUINTERO <jaider_smoreno@soy.sena.edu.co>

JUAN SEBASTIAN MARTINEZ PINTO <sebaspinto96@gmail.com>

MICHAEL STEVEN SALAMANCA MARTIN <salamancamai12@gmail.com>

NICOLAS MARTINEZ VALENZUELA <nicomav1101023@gmail.com>

PAULA ANDREA CASSIANI CASTILLO <paulaacassiani@gmail.com>






