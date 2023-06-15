# **Endpoints**

[Main page](../README.md)

## Auth 
### **Endpoint for user registration:**
>* Method: `POST`.
>* URL: `/register`
>* Parameters of the request:
>	* `full_name`: string - full name of employee
>	* `user_name`: string - employee login in the system
>	* `email`: string
>	* `password`: string
>	* `role`: string - The role of the employee in the system
>* Response:
>	* Successful status: `201 Created`
>```json
>{
>    "status":"success"
>}
>```
>* Errors:
>    * status code: `400 Bad Request`

### **Endpoint for user login:**
>* Method: `POST`.
>* URL: `/login`
>* Parameters of the request:
>	* `user_name`: string - employee login in the system
>	* `password`: string
>* Response:
>	* Successful status: `200 OK`
>```json
>{
>    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4Njc3MjA5MiwianRpIjoiMTA4NDBjZTAtMz>U2ZC00ZmM1LTlkY2EtMTI0MzM1MjQ3Y2UxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX2lkIjoxLCJyb2xlIjoiY2FzaGllciJ9LCJuYmYiOjE2ODY3NzIwOTIsImV4cCI6MTY4Njc3Mjk5Mn0.2TT4p0BCFdQd4R740ZJGJMxRUrHiLvXyMKgt4x8xGxI"
>}
>```
>* Errors:
>    * status code: `400 Bad Request`

## Products
### **Endpoint for adding a product:**
>* Method: `POST`.
>* URL: `/products`
>* Request parameters: 
>    * `product_name`: string
>    * `price`: float
>    * `creation_date`: a string of the format YYYY-MM-DD HH:MM
>* Request Headers
>    * `Authorization` - User authorization token.
>* Response: 
>    * status code: `200 OK`
>```json
>{
>    "status":"success"
>}
>```
>* Errors:
>    * status code: `401 Unauthorized`
>    * status code: `400 Bad Request`

### **Endpoint to retrieve product data:**
>* Method: `GET`.
>* URL: `/products/`
>* Request parameters:
>    * `page`: int (optional) - Results page
>    * `limit`: int (optional) - Maximum number of records per page
>* Request Headers
>    * `Authorization` - User authorization token.
>* Response: 
>    * status code: `200 OK`
>```json
>[
>    {
>        "creation_date": "Fri, 05 May 2023 00:00:00 GMT",
>        "id": 1,
>        "price": 12.5,
>        "product_name": "Raspberry Pi Pico"
>    },
>    {
>        "creation_date": "Mon, 12 Jun 2023 00:00:00 GMT",
>        "id": 2,
>        "price": 14.0,
>        "product_name": "Raspberry Pi Pico W"
>    }
>]
>```
>* Errors:
>    * status code: `401 Unauthorized`
>    * status code: `400 Bad Request`


### **Endpoint for deleting a product:**
>* Method: `DELETE`.
>* URL: `/products/{id}`
>* Request parameters: 
>    * `id`: int - Product ID
>* Request Headers
>    * `Authorization` - User authorization token.
>* Response:
>    * status code: `200 OK`
>```json
>{
>    "status":"success"
>}
>```
>* Errors:
>    * status code: `401 Unauthorized`
>    * status code: `400 Bad Request`

### **Endpoint to update product data:**
>* Method: `PUT`.
>* URL: `/products/{id}`
>* Request parameters: 
>    * `id`: int - Product ID
>    * `product_name`: string (optional) 
>    * `price`: float (optional)
>    * `creation_date`: string (optional) - a string of the format YYYY-MM-DD HH:MM
>* Request Headers
>    * `Authorization` - User authorization token.
>* Response: 
>    * status code: `200 OK`
>```json
>{
>    "status":"success"
>}
>```
>* Errors:
>    * status code: `401 Unauthorized`
>    * status code: `400 Bad Request`

### **Endpoint to retrieve product data (by id):**
>* Method: `GET`.
>* URL: `/products/{id}`
>* Request parameters: 
>    * `id`: int - Product ID
>* Request Headers
>    * `Authorization` - User authorization token.
>* Response: 
>    * status code: `200 OK`
>```json
>{
>    "creation_date": "Fri, 05 May 2023 00:00:00 GMT",
>    "id": 1,
>    "price": 12.5,
>    "product_name": "Raspberry Pi Pico"
>}
>```
>* Errors:
>    * status code: `401 Unauthorized`
>    * status code: `400 Bad Request`

## Invoice
### **Endpoint for invoice generation:**
>* Method: `GET`.
>* URL: `/invoices/{order_id}`
>* Parameters of the request: 
>    * `id`: int - Order ID
>* Request Headers
>    * `Authorization` - User authorization token.
>* Response: 
>    * status code: `200 OK`
>```json
>{
>    "cashier_full_name": "Ivan Ivanov",
>    "cashier_id": 1,
>    "discount": 20.0,
>    "order_date": "Wed, 14 Jun 2023 22:50:49 GMT",
>    "order_id": 1,
>    "price": 12.5,
>    "product_id": 1,
>    "product_name": "Raspberry Pi Pico",
>    "quantity": 2,
>    "total": 20.0
>}
>```
>* Errors:
>    * status code: `401 Unauthorized`
>    * status code: `400 Bad Request`

## Orders
**Endpoint to create an order:**
>* Method: `POST`.
>* URL: `/orders`
>* Parameters of the request: 
>    * `product_id`: int
>    * `order_status`: string 
>    * `discount`:float (optional)
>    * `quantity`: int
>* Request Headers
>    * `Authorization` - User authorization token.
>* Response:
>    * status code: `200 OK`
>```json
>{
>    "status":"success"
>}
>```
>* Errors:
>    * status code: `403 Forbidden`
>    * status code: `401 Unauthorized`
>    * status code: `400 Bad Request`

**Endpoint to retrieve all order data:**
>* Method: `GET`.
>* URL: `/orders`
>* Parameters of the request: 
>    * `page`: int (optional) - Results page
>    * `limit`: int (optional) - Maximum number of records per page
>    * `start_date`: string (optional) - Lower time limit of the sample range, format YYYY-MM-DD HH:MM
>    * `end_date`: string (optional) - Upper time limit of the sample range, format YYYY-MM-DD HH:MM
>* Request Headers
>    * `Authorization` - User authorization token.
>* Response:
>    * status code: `200 OK`
>```json
>[
>    {
>        "cashier_id": 1,
>        "discount": 20.0,
>        "id": 1,
>        "order_date": "Thu, 15 Jun 2023 10:05:30 GMT",
>        "order_status": "pending",
>        "product_id": 1,
>        "quantity": 2
>    },
>    {
>        "cashier_id": 1,
>        "discount": 20.0,
>        "id": 2,
>        "order_date": "Thu, 15 Jun 2023 10:05:37 GMT",
>        "order_status": "pending",
>        "product_id": 2,
>        "quantity": 2
>    },
>    {
>        "cashier_id": 1,
>        "discount": 20.0,
>        "id": 3,
>        "order_date": "Thu, 15 Jun 2023 10:05:41 GMT",
>        "order_status": "pending",
>        "product_id": 3,
>        "quantity": 2
>    }
>]
>```
>* Errors:
>    * status code: `401 Unauthorized`
>    * status code: `400 Bad Request`

**Endpoint to delete an order:**
>* Method: `DELETE`.
>* URL: `/orders/{id}`
>* Parameters of the request:
>    * `id`: int - Order ID
>* Request Headers
>    * `Authorization` - User authorization token.
>* Response:
>    * status code: `200 OK`
>```json
>{
>    "status":"success"
>}
>```
>* Errors:
>    * status code: `401 Unauthorized`
>    * status code: `400 Bad Request`

## Orders
**Endpoint for updating order data:**
>* Method: `PUT`.
>* URL: `/orders/{id}`
>* Parameters of the request: 
>    * `id`: int - Order ID
>    * `product_id`: int (optional)
>    * `cashier_id`: int (optional)
>    * `order_date`: string (optional) - date in the format YYYY-MM-DD HH:MM
>    * `order_status`: string (optional)
>    * `discount`: float (optional)
>    * `quantity`: int (optional)
>* Request Headers
>    * `Authorization` - User authorization token.
>* Response:
>    * status code: `200 OK`
>```json
>{
>    "status":"success"
>}
>```
>* Errors:
>    * status code: `403 Forbidden`
>    * status code: `401 Unauthorized`
>    * status code: `400 Bad Request`

**Endpoint for receiving order data by id:**
>* Method: `GET`.
>* URL: `/orders/{id}`
>* Parameters of the request: 
>    * `id`: int - Order ID
>* Request Headers
>    * `Authorization` - User authorization token.
>* Response:
>    * status code: `200 OK`
>```json
>{
>    "cashier_id": 1,
>    "discount": 20.0,
>    "id": 1,
>    "order_date": "Thu, 15 Jun 2023 10:05:30 GMT",
>    "order_status": "pending",
>    "product_id": 1,
>    "quantity": 2
>}
>```
>* Errors:
>    * status code: `401 Unauthorized`
>    * status code: `400 Bad Request`