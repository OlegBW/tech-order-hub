from sqlalchemy import TEXT, REAL, INTEGER, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from typing import Optional
from .database import Base

'''
Defines database models
'''

print('Import model')

class Product(Base):
    __tablename__ = 'product'
    id = mapped_column(INTEGER, primary_key = True)
    product_name = mapped_column(TEXT, unique = True, nullable = False)
    price = mapped_column(REAL, nullable = False)
    creation_date = mapped_column(TIMESTAMP, nullable = False)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id, self.product_name, self.price, self.creation_date})'


class Employee(Base):
    __tablename__ = 'employee'
    id = mapped_column(INTEGER, primary_key = True)
    full_name = mapped_column(TEXT, nullable = False)
    user_name = mapped_column(TEXT, unique = True, nullable = False)
    email = mapped_column(TEXT, unique = True, nullable = False)
    hashed_password = mapped_column(TEXT, nullable = False)
    user_role = mapped_column(TEXT, nullable = False)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id, self.full_name, self.user_name, self.email, self.hashed_password, self.user_role})'


class OrderInfo(Base):
    __tablename__ = 'order_info'
    id = mapped_column(INTEGER, primary_key = True)
    product_id = mapped_column(ForeignKey('product.id'))
    cashier_id = mapped_column(ForeignKey('employee.id'))
    order_status = mapped_column(TEXT, nullable = False)
    order_date = mapped_column(TIMESTAMP, nullable = False)
    discount = mapped_column(REAL, nullable = False)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id, self.product_id, self.cashier_id, self.order_status, self.order_date, self.discount})'