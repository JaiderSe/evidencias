from app.utils.db import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'pedidos'
    
    pedido_id = db.Column(db.Integer, primary_key=True)
    mesa_id = db.Column(db.Integer, db.ForeignKey('mesas.mesa_id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    fecha_hora = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(20), nullable=False)
    notas = db.Column(db.Text)
    total = db.Column(db.Numeric(10, 2))
    
    # Relación con detalles
    detalles = db.relationship('OrderDetail', backref='pedido', lazy=True)
    
    def __repr__(self):
        return f'<Order {self.pedido_id}>'