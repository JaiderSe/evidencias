from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DecimalField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class RegistrationForm(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Contraseña', 
                                   validators=[DataRequired(), EqualTo('password')])
    rol = SelectField('Rol', choices=[
        ('mesero', 'Mesero'), 
        ('chef', 'Chef'), 
        ('inventario', 'Inventario'),
        ('administrador', 'Administrador')
    ], validators=[DataRequired()])
    submit = SubmitField('Registrarse')

class DishForm(FlaskForm):
    nombre = StringField('Nombre del Platillo', validators=[DataRequired()])
    category_id = SelectField('Categoría', coerce=int, validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    precio = DecimalField('Precio', validators=[DataRequired(), NumberRange(min=0)])
    tiempo_preparacion = IntegerField('Tiempo de Preparación (minutos)', 
                                    validators=[NumberRange(min=1)])
    activo = BooleanField('Disponible', default=True)
    es_vegano = BooleanField('Es Vegano')
    es_vegetariano = BooleanField('Es Vegetariano')
    tiene_gluten = BooleanField('Contiene Gluten', default=True)
    nivel_picante = SelectField('Nivel de Picante', choices=[
        (0, 'Nada picante'), 
        (1, 'Ligero'), 
        (2, 'Moderado'),
        (3, 'Picante'),
        (4, 'Muy picante'),
        (5, 'Extremo')
    ], coerce=int, default=0)
    submit = SubmitField('Guardar')

class CategoryForm(FlaskForm):
    nombre = StringField('Nombre de la Categoría', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    orden_menu = IntegerField('Orden en el Menú', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class OrderForm(FlaskForm):
    mesa_id = SelectField('Mesa', coerce=int, validators=[DataRequired()])
    notas = TextAreaField('Notas Especiales')
    platillos = SelectField('Platillos', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Crear Pedido')

class InventoryMovementForm(FlaskForm):
    ingredient_id = SelectField('Ingrediente', coerce=int, validators=[DataRequired()])
    cantidad = DecimalField('Cantidad', validators=[DataRequired(), NumberRange(min=0.01)])
    tipo_movimiento = SelectField('Tipo de Movimiento', choices=[
        ('entrada', 'Entrada'), 
        ('salida', 'Salida'), 
        ('ajuste', 'Ajuste')
    ], validators=[DataRequired()])
    motivo = StringField('Motivo', validators=[DataRequired()])
    costo_total = DecimalField('Costo Total', validators=[NumberRange(min=0)])
    submit = SubmitField('Registrar Movimiento')