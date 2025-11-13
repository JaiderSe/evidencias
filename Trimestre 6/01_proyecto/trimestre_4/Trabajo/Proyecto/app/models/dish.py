from app.utils.db import db

class Dish(db.Model):
    __tablename__ = 'platillos'
    
    platillo_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.categoria_id'))
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Numeric(10,2), nullable=False)
    tiempo_preparacion = db.Column(db.Integer)
    activo = db.Column(db.Boolean, default=True)
    
    # Relaciones
    categoria = db.relationship('Category', backref='platillos')
    ingredientes = db.relationship('Ingredient', secondary='platillo_ingredientes', backref='platillos')
    
    def to_dict(self):
        return {
            'id': self.platillo_id,
            'nombre': self.nombre,
            'precio': float(self.precio),
            'descripcion': self.descripcion,
            'tiempo_preparacion': self.tiempo_preparacion
        }