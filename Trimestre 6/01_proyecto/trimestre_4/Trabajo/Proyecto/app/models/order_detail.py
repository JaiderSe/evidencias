from app.utils.db import db

class OrderDetail(db.Model):
    __tablename__ = 'detalles_pedido'
    
    detalle_id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'))
    platillo_id = db.Column(db.Integer, db.ForeignKey('platillos.platillo_id'))
    cantidad = db.Column(db.Integer, nullable=False, default=1)
    precio_unitario = db.Column(db.Numeric(10, 2), nullable=False)
    personalizaciones = db.Column(db.Text)
    estado = db.Column(db.String(20), default='pendiente')
    notas_chef = db.Column(db.Text)
    
    def __repr__(self):
        return f'<OrderDetail {self.detalle_id}>'