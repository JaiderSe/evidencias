from app.utils.db import db

class Ingredient(db.Model):
    __tablename__ = 'ingredientes'
    
    ingrediente_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    unidad_medida = db.Column(db.String(20), nullable=False)
    stock_actual = db.Column(db.Numeric(10, 2), nullable=False)
    stock_minimo = db.Column(db.Numeric(10, 2), nullable=False)
    proveedor_principal = db.Column(db.String(100))
    costo_por_unidad = db.Column(db.Numeric(10, 2))
    caduca = db.Column(db.Boolean, default=False)
    dias_caducidad = db.Column(db.Integer)
    
    # Relaciones
    platillos = db.relationship('Dish', secondary='platillo_ingredientes', back_populates='ingredientes')
    movimientos = db.relationship('InventoryMovement', backref='ingrediente', lazy=True)
    
    def __repr__(self):
        return f'<Ingredient {self.nombre}>'