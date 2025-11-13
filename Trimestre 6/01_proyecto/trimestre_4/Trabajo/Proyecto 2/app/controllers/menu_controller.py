from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.services.menu_service import MenuService
from app.forms import DishForm, CategoryForm
from app.utils.decorators import role_required

menu_bp = Blueprint('menu', __name__, url_prefix='/menu')
service = MenuService()

@menu_bp.route('/')
@login_required
def list_dishes():
    category_id = request.args.get('category_id')
    dishes = service.get_all_dishes(category_id)
    categories = service.get_all_categories()
    return render_template('menu/list.html', 
                         dishes=dishes, 
                         categories=categories,
                         current_category=category_id)

@menu_bp.route('/create', methods=['GET', 'POST'])
@login_required
@role_required('chef', 'administrador')
def create_dish():
    form = DishForm()
    form.category_id.choices = [(c.categoria_id, c.nombre) for c in service.get_all_categories()]
    
    if form.validate_on_submit():
        dish_data = {
            'nombre': form.nombre.data,
            'categoria_id': form.category_id.data,
            'descripcion': form.descripcion.data,
            'precio': form.precio.data,
            'tiempo_preparacion': form.tiempo_preparacion.data,
            'activo': form.activo.data,
            'es_vegano': form.es_vegano.data,
            'es_vegetariano': form.es_vegetariano.data,
            'tiene_gluten': form.tiene_gluten.data,
            'nivel_picante': form.nivel_picante.data
        }
        service.create_dish(dish_data)
        flash('Platillo creado exitosamente', 'success')
        return redirect(url_for('menu.list_dishes'))
    
    return render_template('menu/create.html', form=form)

@menu_bp.route('/<int:id>')
@login_required
def detail_dish(id):
    dish = service.get_dish_by_id(id)
    if not dish:
        flash('Platillo no encontrado', 'danger')
        return redirect(url_for('menu.list_dishes'))
    return render_template('menu/detail.html', dish=dish)

@menu_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@role_required('chef', 'administrador')
def edit_dish(id):
    dish = service.get_dish_by_id(id)
    if not dish:
        flash('Platillo no encontrado', 'danger')
        return redirect(url_for('menu.list_dishes'))
    
    form = DishForm(obj=dish)
    form.category_id.choices = [(c.categoria_id, c.nombre) for c in service.get_all_categories()]
    
    if form.validate_on_submit():
        dish_data = {
            'nombre': form.nombre.data,
            'categoria_id': form.category_id.data,
            'descripcion': form.descripcion.data,
            'precio': form.precio.data,
            'tiempo_preparacion': form.tiempo_preparacion.data,
            'activo': form.activo.data,
            'es_vegano': form.es_vegano.data,
            'es_vegetariano': form.es_vegetariano.data,
            'tiene_gluten': form.tiene_gluten.data,
            'nivel_picante': form.nivel_picante.data
        }
        service.update_dish(id, dish_data)
        flash('Platillo actualizado exitosamente', 'success')
        return redirect(url_for('menu.detail_dish', id=id))
    
    return render_template('menu/edit.html', form=form, dish=dish)

@menu_bp.route('/categories', methods=['GET', 'POST'])
@login_required
@role_required('administrador')
def manage_categories():
    form = CategoryForm()
    if form.validate_on_submit():
        category_data = {
            'nombre': form.nombre.data,
            'descripcion': form.descripcion.data,
            'orden_menu': form.orden_menu.data
        }
        service.create_category(category_data)
        flash('Categoría creada exitosamente', 'success')
        return redirect(url_for('menu.manage_categories'))
    
    categories = service.get_all_categories()
    return render_template('menu/categories.html', form=form, categories=categories)