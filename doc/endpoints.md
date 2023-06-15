# **Endpoints**

[Main page](../README.md)

## Auth 
### **Endpoint for user registration:**
>* Method: `POST`.
>* URL: `/register`
>* Parameters of the request:
>	* `name` 
>	* `login`
>	* `email`
>	* `password`
>	* `role`
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
>	* `e-mail`
>	* `password`
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
>    * `product_name` 
>    * `price`
>    * `creation_date`
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
>    * `page` (optional) - Results page
>    * `limit` (optional) - Maximum number of records per page
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
>    * `id` - Product ID
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

### **Endpoint to update product data:**.
>* Method: `PUT`.
>* URL: `/products/{id}`
>* Request parameters: 
>    * `id` - Product ID
>    * `product_name` (optional) 
>    * `price` (optional)
>    * `creation_date` (optional)
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
>    * `id` - Product ID
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
### **Endpoint for invoice generation:**.
>* Method: `GET`.
>* URL: `/invoices/{order_id}`
>* Parameters of the request: 
>    * `id` - Order ID
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