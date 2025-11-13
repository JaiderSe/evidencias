from app.utils.db import db

class InventoryMovement(db.Model):
    __tablename__ = 'inventario'
    
    movimiento_id = db.Column(db.Integer, primary_key=True)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingredientes.ingrediente_id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    cantidad = db.Column(db.Numeric(10, 2), nullable=False)
    tipo_movimiento = db.Column(db.String(10), nullable=False)
    fecha = db.Column(db.DateTime, server_default=db.func.now())
    motivo = db.Column(db.Text)
    costo_total = db.Column(db.Numeric(10, 2))
    
    def __repr__(self):
        return f'<InventoryMovement {self.movimiento_id}>'