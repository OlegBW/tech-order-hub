from flask import Blueprint, request, abort, jsonify
from markupsafe import escape  
from argon2 import PasswordHasher
from .database import db_session
from .models import Employee

'''
Implementation of registration functionality using Argon2 hashing

registration()
'''

ph = PasswordHasher()

registration_blueprint = Blueprint('registration_blueprint', __name__, url_prefix='/auth')

@registration_blueprint.route('/registration', methods = ['POST'])
def registration():
    '"/auth/registration" request handler'
    full_name = request.form.get('full_name')
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password')
    role = request.form.get('role')

    if full_name is None:
        abort(400)

    if user_name is None:
        abort(400)

    if email is None:
        abort(400)

    if password is None:
        abort(400)

    if role is None:
        abort(400)

    full_name = escape(full_name)
    user_name = escape(user_name)
    email = escape(email)
    password = escape(password)
    role = escape(role)

    password = ph.hash(password)

    criteria = db_session.query(Employee).filter_by(user_name = user_name, email = email).exists()
    is_exists = db_session.query(criteria).scalar()

    if is_exists:
        abort(400)
        
    else:
        new_employee = Employee(
            full_name = full_name, 
            user_name = user_name, 
            email = email, 
            hashed_password = password, 
            user_role = role
            )
        
        db_session.add(new_employee)
        db_session.commit()

    return jsonify({"status": "success"})