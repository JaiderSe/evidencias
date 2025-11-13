from app.utils.db import db

class Customer(db.Model):
    __tablename__ = 'clientes'
    
    cliente_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))
    preferencias = db.Column(db.Text)
    fecha_registro = db.Column(db.DateTime, server_default=db.func.now())
    
    # Relaciones
    pedidos = db.relationship('Order', backref='cliente', lazy=True)
    favoritos = db.relationship('Dish', secondary='favoritos_clientes', backref='clientes_favoritos')
    
    def __repr__(self):
        return f'<Customer {self.nombre}>'