from flask import Blueprint, abort, request, jsonify
from markupsafe import escape
from .database import db_session
from .models import Product, OrderInfo, Employee
from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime

'''
Implements the functionality of CRUD operations for orders

Functions:
'''

orders_blueprint = Blueprint('orders_blueprint', __name__)

@orders_blueprint.route('/orders', methods = ['GET', 'POST'])
@jwt_required()
def orders_CR():
    if request.method == 'GET':
        orders_data = None

        page = request.args.get('page')
        limit = request.args.get('limit')

        if not (page is None or limit is None):
            try:
                page = int(page)
                limit = int(limit)
            except Exception:
                abort(400)
            orders_data = db_session.query(OrderInfo).limit(limit = limit).offset(offset = page * limit).all()
        else:
            orders_data = db_session.query(OrderInfo).all()

        response = []
        
        for order in orders_data:
            response.append({
                'id': order.id,
                'product_id': order.product_id,
                'cashier_id': order.cashier_id,
                'order_status': order.order_status,
                'order_date': order.order_date,
                'discount': order.discount,
                'quantity': order.quantity
            })

        return jsonify(response)

    elif request.method == 'POST':
        user_data = get_jwt_identity()
        if user_data.get('role') != 'cashier':
            abort(400)

        cashier_id = user_data.get('user_id')

        product_id = request.form.get('product_id')
        order_status = request.form.get('order_status')
        order_date = request.form.get('order_date')
        discount = request.form.get('discount')
        quantity = request.form.get('quantity')

        if product_id is None:
            abort(400)

        if order_status is None:
            abort(400)

        if order_date is None:
            abort(400)

        if discount is None:
            abort(400)

        if quantity is None:
            abort(400)

        product_id = escape(product_id)
        order_status = escape(order_status)
        order_date = escape(order_date)
        discount = escape(discount)
        quantity = escape(quantity)

        date_format = "%Y-%m-%d %H:%M"
        try:
            order_date = datetime.datetime.strptime(order_date, date_format)
        except Exception:
            return jsonify({"status": "wrong date format, YYYY-MM-DD HH:MM required"})

        product = db_session.query(Product).get(product_id)
        if product is None:
            abort(400)

        cashier = db_session.query(Product).get(cashier_id)
        if cashier is None:
            abort(400)

        criteria = db_session.query(OrderInfo).filter_by(
            product_id = product_id, 
            cashier_id = cashier_id,
            order_status = order_status,
            order_date = order_date,
            discount = discount,
            quantity = quantity
            ).exists()
        is_exists = db_session.query(criteria).scalar()

        if is_exists:
            abort(400)

        new_order = OrderInfo(
            product_id = product_id, 
            cashier_id = cashier_id,
            order_status = order_status,
            order_date = order_date,
            discount = discount,
            quantity = quantity
        )
        db_session.add(new_order)
        db_session.commit()

        return jsonify({"status": "success"})


@orders_blueprint.route('/orders/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
@jwt_required()
def orders_RUD(id):
    if request.method == 'GET':
        order_data = db_session.query(OrderInfo).get(id)
        if order_data is None:
            abort(400)

        response = {
            'id': order_data.id,
            'product_id': order_data.product_id,
            'cashier_id': order_data.cashier_id,
            'order_status': order_data.order_status,
            'order_date': order_data.order_date,
            'discount': order_data.discount,
            'quantity': order_data.quantity
        }
        return jsonify(response)
    
    elif request.method == 'PUT':
        product_id = request.form.get('product_id')
        cashier_id = request.form.get('cashier_id')
        order_status = request.form.get('order_status')
        order_date = request.form.get('order_date')
        discount = request.form.get('discount')
        quantity = request.form.get('quantity')

        order_data = db_session.query(OrderInfo).get(id)
        if order_data is None:
            abort(400)

        fields_arr = [product_id, cashier_id, order_status, order_date, discount, quantity]
        is_valid = bool(len([field for field in fields_arr if not (field is None)]))
        if not is_valid:
            return jsonify({"status": "no data"})
        
        if not (product_id is None):
            product_id = escape(product_id)
            product = db_session.query(Product).get(product_id)
            if not (product is None):
                order_data.product_id = product_id

        if not (cashier_id is None):
            cashier_id = escape(cashier_id)
            cashier = db_session.query(Employee).get(cashier_id)
            if not (cashier is None):
                order_data.cashier_id = cashier_id

        if not (order_status is None):
            order_status = escape(order_status)
            order_data.order_status = order_status

        if not (order_date is None):
            order_date = escape(order_date)
            
            date_format = "%Y-%m-%d %H:%M"
            try:
                order_date = datetime.datetime.strptime(order_date, date_format)
            except Exception:
                return jsonify({"status": "wrong date format, YYYY-MM-DD HH:MM required"})

            order_data.order_date = order_date

        if not (discount is None):
            discount = escape(discount)
            order_data.discount = discount

        if not (quantity is None):
            quantity = escape(quantity)
            order_data.quantity = quantity

        db_session.commit()
        return jsonify({"status": "success"})

    elif request.method == 'DELETE':
        order_data = db_session.query(OrderInfo).get(id)
        if order_data is None:
            abort(400)

        db_session.delete(order_data)
        db_session.commit()
        return jsonify({"status": "success"})