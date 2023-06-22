from flask import Blueprint, abort, jsonify
from .database import db_session
from .models import OrderInfo
from flask_jwt_extended import jwt_required

'''
Implements the functionality of generating invoice data 

Functions:

invoice_generator(id)
'''

invoices_blueprint = Blueprint('invoices_blueprint', __name__)

@invoices_blueprint.route('/invoices/<int:id>', methods=['GET'])
@jwt_required()
def invoice_generator(id):
    'Generates JSON with invoice data'

    order_data = db_session.query(OrderInfo).get(id)
    if order_data is None:
        abort(400)
    
    product_data = order_data.product
    if product_data is None:
        abort(400)

    employee_data = order_data.employee
    if employee_data is None:
        abort(400)

    total_price = product_data.price * order_data.quantity
    total_discount = product_data.price * order_data.quantity * (order_data.discount / 100)

    invoice_data = {
        "order_id": order_data.id,
        "product_id": order_data.product_id,
        "product_name": product_data.product_name,
        "price": product_data.price,
        "quantity": order_data.quantity,
        "discount": order_data.discount,
        "order_date": order_data.order_date,
        "total": round(total_price - total_discount, 2),
        "cashier_id": order_data.cashier_id,
        "cashier_full_name": employee_data.full_name,
    }

    return jsonify(invoice_data)