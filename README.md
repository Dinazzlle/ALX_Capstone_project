
E-Commerce API
Overview
The E-Commerce API is a backend service designed to manage products and categories for an e-commerce platform. It supports secure CRUD operations using token-based authentication with Django REST Framework (DRF) and SimpleJWT.

Features
Products Management: Create, read, update, and delete products.
Categories Management: Manage product categories.
User Authentication: Secure access using JSON Web Tokens (JWT).
Role-Based Permissions: Restricted access to sensitive endpoints.
Token Operations: Obtain and refresh tokens for secure sessions.
Tech Stack
Programming Language: Python
Framework: Django, Django REST Framework
Authentication: SimpleJWT
Database: SQLite (default, replaceable with PostgreSQL or MySQL)
Installation
1. Clone the Repository
bash
git clone https://github.com/Dinazzlle/ALX_Capstone_project.git
cd my_django_project
2. Create a Virtual Environment
bash
python -m venv venv
venv\Scripts\activate    
3. Install Dependencies
bash
pip install -r requirements.txt
4. Apply Migrations
python manage.py makemigrations
python manage.py migrate
5. Run the Development Server
bash

python manage.py runserver
API Endpoints
Authentication
Obtain Token:
POST http://127.0.0.1:8000/api/token/
Request Body:
json

{
    "username": "user1",
    "password": "password1"
}
Response:
json

{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
Refresh Token:
POST http://127.0.0.1:8000/api/token/refresh/
Request Body:
json
{
    "refresh": "<refresh_token>"
}
Response:
json
{
    "access": "<new_access_token>"
}
Products
List Products:

GET http://127.0.0.1:8000/api/products/
Headers: Authorization: Bearer <access_token>
Create Product:

POST /api/products/
Headers: Authorization: Bearer <access_token>
Request Body:
json
{
    "name": "Product Name",
    "price": 100.0,
    "stock_quantity": 50,
    "category": 1
}
Retrieve Product:

GET http://127.0.0.1:8000/api/products/<id>/
Headers: Authorization: Bearer <access_token>
Update Product:

PUT http://127.0.0.1:8000/api/products/<id>/
Headers: Authorization: Bearer <access_token>
Request Body: Similar to Create Product
Delete Product:

DELETE /api/products/<id>/
Headers: Authorization: Bearer <access_token>
Categories
List Categories:

GET /api/categories/
Headers: Authorization: Bearer <access_token>
Create Category:

POST /api/categories/
Headers: Authorization: Bearer <access_token>
Request Body:
json
Copy code
{
    "name": "Category Name"
}
Retrieve Category:

GET /api/categories/<id>/
Headers: Authorization: Bearer <access_token>
Update Category:

PUT /api/categories/<id>/
Headers: Authorization: Bearer <access_token>
Request Body: Similar to Create Category
Delete Category:

DELETE /api/categories/<id>/
Headers: Authorization: Bearer <access_token>
Authentication Setup
JWT Authentication
The API uses SimpleJWT for authentication.

Add the following to your settings.py:
python
Copy code
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
Use the provided endpoints to obtain and refresh tokens.
Testing
Tools
Use Postman or cURL to test API endpoints.
Example Commands
Obtain Token:
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "user1", "password": "password1"}'
Access Protected Endpoint:
bash
Copy code
curl -X GET http://127.0.0.1:8000/api/products/ \
     -H "Authorization: Bearer <access_token>"
Future Enhancements
Role-Based Access Control: Assign roles such as admin, seller, and customer.
Search and Filtering: Add query parameters for products and categories.
Improved Error Handling: Provide detailed error messages for invalid requests.
Contributing
Contributions are welcome! Please create a pull request or raise an issue in the repository.


Repository Link
(https://github.com/Dinazzlle/ALX_Capstone_project.git)