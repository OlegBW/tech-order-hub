from flask import Blueprint, abort, request, jsonify
from markupsafe import escape
from argon2 import PasswordHasher
from .database import db_session
from .models import Employee
from flask_jwt_extended import create_access_token

'''
Implements login functionality with verification of Argon2 hashed passwords

Functions:

login()
'''

ph = PasswordHasher()

login_blueprint = Blueprint('login_blueprint', __name__, url_prefix='/auth')

@login_blueprint.route('/login', methods = ['POST'])
def login():
    '"/auth/login" request handler'

    user_name = request.form.get('user_name')
    password = request.form.get('password')

    if user_name is None:
        abort(400)

    elif password is None:
        abort(400)

    user_name = escape(user_name)
    password = escape(password)

    user_data = db_session.query(Employee).filter_by(user_name = user_name).first()

    if not user_data:
        abort(401)

    is_valid = ph.verify(user_data.hashed_password, password)

    if not is_valid:
        abort(401)

    access_token = create_access_token(identity = {'user_id': user_data.id, 'role': user_data.user_role})
    return jsonify(access_token = access_token)
