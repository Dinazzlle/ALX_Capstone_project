# **Securing the API with Authentication**

This document outlines the implementation of authentication for the API, the setup process, and testing instructions.

---

## **Authentication Method**

I have implemented **token-based authentication** using the Django REST Framework (DRF). The authentication mechanism ensures that only authorized users can access or manipulate the resources exposed by the API.

---

## **Steps to Implement Authentication**

### **1\. Install Required Packages**

the Django REST Framework and SimpleJWT (for token-based authentication) are installed:

pip install djangorestframework djangorestframework-simplejwt

### **2\. Update Django Settings**

Modified `settings.py` to configure REST framework and SimpleJWT:

\# settings.py

INSTALLED\_APPS \+= \[  
    'rest\_framework',  
\]

REST\_FRAMEWORK \= {  
    'DEFAULT\_AUTHENTICATION\_CLASSES': \[  
        'rest\_framework\_simplejwt.authentication.JWTAuthentication',  
    \],  
    'DEFAULT\_PERMISSION\_CLASSES': \[  
        'rest\_framework.permissions.IsAuthenticated',  
    \],  
}

### **3\. Add Token Generation and Refresh Endpoints**

Included SimpleJWT views in my `ecommerce/urls.py` to allow users to obtain and refresh tokens:

from rest\_framework\_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns \+= \[  
    path('api/token/', TokenObtainPairView.as\_view(), name='token\_obtain\_pair'),  
    path('api/token/refresh/', TokenRefreshView.as\_view(), name='token\_refresh'),  
\]

### **4\. Secure API Views**

Ensured the API views requires authentication by setting permissions. `products/views.py`:

from rest\_framework.permissions import IsAuthenticated

class ProductViewSet(ModelViewSet):  
    queryset \= Product.objects.all()  
    serializer\_class \= ProductSerializer  
    permission\_classes \= \[IsAuthenticated\]  \# Require authentication for all operations

class CategoryViewSet(ModelViewSet):  
    queryset \= Category.objects.all()  
    serializer\_class \= CategorySerializer  
    permission\_classes \= \[IsAuthenticated\]

To allow unauthenticated access to certain endpoints, I overrided the permission classes for specific views:

from rest\_framework.permissions import AllowAny

class UserRegisterView(generics.CreateAPIView):  
    queryset \= User.objects.all()  
    serializer\_class \= UserRegisterSerializer  
    permission\_classes \= \[AllowAny\]  \# Allow anyone to register

### **5\. Test Authentication Locally**

Run the server:  
 python manage.py runserver

1. 

Obtain a token:  
 curl \-X POST http://127.0.0.1:8000/api/token/ \\  
    \-H "Content-Type: application/json" \\  
    \-d '{"username": "\<your\_username\>", "password": "\<your\_password\>"}'  
 Expected Response:  
 {  
    "refresh": "\<refresh\_token\>",  
    "access": "\<access\_token\>"  
}

2. 

Used the token to access protected endpoints:  
 curl \-H "Authorization: Bearer \<access\_token\>" http://127.0.0.1:8000/api/products/

3. 

---

## **Testing Instructions**

### **Prerequisites**

* I should have an admin user or register a new user via `/api/register/`.  
* Obtain a valid JWT token from `/api/token/`.

### **Testing Steps**

1. **Access Protected Endpoint Without Token:**

   * Send a GET request to `/api/products/`.

Expected Response:  
 {  
    "detail": "Authentication credentials were not provided."  
}

*   
2. **Access Protected Endpoint With Token:**

   * Use the access token in the `Authorization` header.

Expected Response:  
 \[  
    {  
        "id": 1,  
        "name": "Product 1",  
        "price": 100.0,  
        "stock\_quantity": 50,  
        "category": "Category 1"  
    }  
\]

*   
3. **Test Token Refresh:**

   * Send a POST request to `/api/token/refresh/` with the refresh token.

Expected Response:  
 {  
    "access": "\<new\_access\_token\>"  
}

* 

---

## **GitHub Repository**

The code implementing the authentication setup is available in the following GitHub repository: [https://github.com/Dinazzlle/ALX\_Capstone\_project.git](https://github.com/Dinazzlle/ALX_Capstone_project.git)  
 Please refer to the `README.md` file in the repository for additional setup instructions.

