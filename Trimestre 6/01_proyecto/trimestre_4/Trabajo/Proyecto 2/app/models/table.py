from app.utils.db import db

class Table(db.Model):
    __tablename__ = 'mesas'
    
    mesa_id = db.Column(db.Integer, primary_key=True)
    numero_mesa = db.Column(db.String(10), unique=True, nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(50))
    estado = db.Column(db.String(20), default='disponible')
    
    # Relación con pedidos
    pedidos = db.relationship('Order', backref='mesa', lazy=True)
    
    def __repr__(self):
        return f'<Table {self.numero_mesa}>'