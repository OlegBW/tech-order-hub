# **Tech Order Hub**

![box.png](./doc/images/box.png)

>**Backend of the order processing system for a hardware store: managing, processing, and tracking orders.**

## Overview
**Tech Order Hub** is a server-based system for automating order management in a hardware store. It provides sales assistants, cashiers, and accountants with a convenient and efficient tool for order processing and reporting.

As part of the Tech Order Hub system:

* Cashiers receive orders from customers and quickly add them to the database.
* Sales consultants have access to created orders to process and update the status to "completed".
* Cashiers can generate invoices, accept payments from customers, and update the order status to "paid".
* Accountants have a complete overview of all orders, their statuses, dates, and discounts, and can generate reports for a specified period.

Each product in the Tech Order Hub system has a name, price, and creation date. To encourage sales of older products, the system automatically provides a 20% discount on products with a creation date that is more than one month from the current date.

The invoice generated by the system contains product details (name, price) and information about the date of order creation and the date of invoice creation.

Tech Order Hub provides a convenient and reliable tool for efficient order management, payment processing, discounting, and reporting.

## Installation and startup
### Loading dependencies:
```sh
sudo chmod +x ./setup.sh
./setup.sh
```

or 

```sh
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
deactivate
```

### Running:

```sh
. venv/bin/activate
flask --app order-hub run
```

### Initializing the database

```sh
flask --app order-hub init-db
```

Use the `--add-fixtures` flag to add product fixtures

[Database structure](./doc/database.md)

[Endpoints](./doc/endpoints.md)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/27788164-f869e23f-cfed-4aca-97fc-fad639b28431?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D27788164-f869e23f-cfed-4aca-97fc-fad639b28431%26entityType%3Dcollection%26workspaceId%3De5f8c7f4-ce4c-48cf-9709-68c6104c55bb)