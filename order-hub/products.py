from flask import Blueprint, abort, request, jsonify
from markupsafe import escape
from .database import db_session
from .models import Product
from flask_jwt_extended import jwt_required
import datetime

'''
Implements the functionality of CRUD operations for products

Functions:

products_CR()
products_RUD(id)
'''

products_blueprint = Blueprint('products_blueprint', __name__)

@products_blueprint.route('/products', methods = ['GET', 'POST'])
@jwt_required()
def products_CR():
    'Performs operations to receive and add product data (C - create, R - read)'

    if request.method == 'GET':
        products_data = None

        page = request.args.get('page')
        limit = request.args.get('limit')

        if not (page is None or limit is None):
            try:
                page = int(page)
                limit = int(limit)
            except Exception:
                abort(400)
            products_data = db_session.query(Product).limit(limit = limit).offset(offset = page * limit).all()
        else:
            products_data = db_session.query(Product).all()

        response = []
        for product in products_data:
            response.append({
                'id': product.id,
                'product_name': product.product_name,
                'price': product.price,
                'creation_date': product.creation_date
            })

        return jsonify(response)

    elif request.method == 'POST':
        product_name = request.form.get('product_name')
        price = request.form.get('price')
        creation_date = request.form.get('creation_date')

        if product_name is None:
            abort(400)

        if price is None:
            abort(400)

        if creation_date is None:
            abort(400)

        product_name = escape(product_name)
        price = escape(price)
        creation_date = escape(creation_date)

        try:
            price = float(price)
        except Exception:
            return jsonify({"status": "wrong price"})

        date_format = "%Y-%m-%d %H:%M"
        try:
            creation_date = datetime.datetime.strptime(creation_date, date_format)
        except Exception:
            return jsonify({"status": "wrong date format, YYYY-MM-DD HH:MM required"})

        criteria = db_session.query(Product).filter_by(product_name = product_name, price = price, creation_date = creation_date).exists()
        is_exists = db_session.query(criteria).scalar()

        if is_exists:
            abort(400)

        new_product = Product(product_name = product_name, price = price, creation_date = creation_date)
        db_session.add(new_product)
        db_session.commit()

        return jsonify({"status": "success"})


@products_blueprint.route('/products/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
@jwt_required()
def products_RUD(id):
    'Implements the functionality of processing a specific product (R - read, U - update, D - delete)'

    if request.method == 'GET':
        product_data = db_session.query(Product).get(id)
        if product_data is None:
            abort(400)

        response = {
            'id': product_data.id,
            'product_name': product_data.product_name,
            'price': product_data.price,
            'creation_date': product_data.creation_date
        }

        return jsonify(response)

    elif request.method == 'PUT':
        product_name = request.form.get('product_name')
        price = request.form.get('price')
        creation_date = request.form.get('creation_date')

        product_data = db_session.query(Product).get(id)
        if product_data is None:
            abort(400)

        if not (product_name or price or creation_date):
            return jsonify({"status": "no data"})

        if not (product_name is None):
            product_name = escape(product_name)
            product_data.product_name = product_name

        if not (price is None):
            price = escape(price)
            try:
                price = float(price)
            except Exception:
                return jsonify({"status": "wrong price"})
            product_data.price = price

        if not (creation_date is None):
            creation_date = escape(creation_date)
            date_format = "%Y-%m-%d %H:%M"
            try:
                creation_date = datetime.datetime.strptime(creation_date, date_format)
            except Exception:
                return jsonify({"status": "wrong date format, YYYY-MM-DD HH:MM required"})
            
            product_data.creation_date = creation_date
        
        db_session.commit()
        return jsonify({"status": "success"})

    elif request.method == 'DELETE':
        product_data = db_session.query(Product).get(id)
        if product_data is None:
            abort(400)
        db_session.delete(product_data)
        db_session.commit()
        return jsonify({"status": "success"})