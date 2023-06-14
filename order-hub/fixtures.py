from . import models
import datetime

def create_products_fixtures():
    'Creates and returns product entity fixtures '

    fixtures = [
        {
            'product_name': 'iPhone 13 Pro',
            'price': 1099.99,
            'creation_date': datetime.datetime(2022, 9, 14, 10, 30)
        },
        {
            'product_name': 'Samsung Galaxy S21',
            'price': 899.99,
            'creation_date': datetime.datetime(2021, 2, 5, 14, 45)
        },
        {
            'product_name': 'Sony PlayStation 5',
            'price': 499.99,
            'creation_date': datetime.datetime(2020, 11, 12, 9, 15)
        },
        {
            'product_name': 'Apple MacBook Pro',
            'price': 1999.99,
            'creation_date': datetime.datetime(2021, 6, 25, 11, 0)
        },
        {
            'product_name': 'Dell XPS 13',
            'price': 1299.99,
            'creation_date': datetime.datetime(2022, 3, 7, 16, 20)
        },
        {
            'product_name': 'Samsung QLED 4K TV',
            'price': 1499.99,
            'creation_date': datetime.datetime(2021, 8, 19, 13, 10)
        },
        {
            'product_name': 'Bose QuietComfort 35 II',
            'price': 299.99,
            'creation_date': datetime.datetime(2020, 7, 2, 10, 5)
        },
        {
            'product_name': 'GoPro HERO9 Black',
            'price': 449.99,
            'creation_date': datetime.datetime(2020, 10, 8, 15, 30)
        },
        {
            'product_name': 'Nintendo Switch',
            'price': 299.99,
            'creation_date': datetime.datetime(2017, 3, 3, 9, 45)
        },
        {
            'product_name': 'LG OLED 4K TV',
            'price': 1799.99,
            'creation_date': datetime.datetime(2022, 1, 20, 12, 15)
        },
        {
            'product_name': 'Canon EOS R5',
            'price': 3799.99,
            'creation_date': datetime.datetime(2020, 7, 9, 14, 0)
        },
        {
            'product_name': 'Microsoft Xbox Series X',
            'price': 499.99,
            'creation_date': datetime.datetime(2020, 11, 10, 8, 30)
        },
        {
            'product_name': 'Apple AirPods Pro',
            'price': 249.99,
            'creation_date': datetime.datetime(2019, 10, 30, 17, 50)
        },
        {
            'product_name': 'Google Pixel 6 Pro',
            'price': 899.99,
            'creation_date': datetime.datetime(2023, 1, 5, 9, 30)
        },
        {
            'product_name': 'Sony WH-1000XM4',
            'price': 349.99,
            'creation_date': datetime.datetime(2020, 9, 1, 11, 20)
        },
        {
            'product_name': 'HP Spectre x360',
            'price': 1399.99,
            'creation_date': datetime.datetime(2021, 4, 16, 15, 10)
        },
        {
            'product_name': 'Nikon D850',
            'price': 2999.99,
            'creation_date': datetime.datetime(2017, 8, 24, 10, 45)
        },
        {
            'product_name': 'Amazon Echo Dot',
            'price': 49.99,
            'creation_date': datetime.datetime(2018, 6, 15, 13, 5)
        },
        {
            'product_name': 'Samsung Galaxy Watch 4',
            'price': 299.99,
            'creation_date': datetime.datetime(2022, 7, 30, 16, 15)
        },
        {
            'product_name': 'Lenovo ThinkPad X1 Carbon',
            'price': 1699.99,
            'creation_date': datetime.datetime(2023, 3, 12, 11, 0)
        }
    ]

    results = []
    for fixture_data in fixtures:
        results.append(models.Product(**fixture_data))

    return results