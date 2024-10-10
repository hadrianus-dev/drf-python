# DRF-Python
## Django Rest Framework

This a Django project with objective of knowledge transmission in Python, specificaly API with Django

STEPS TO FOLOW:
1. Install Django
2. Start Django Project
    ```python
    django-admin startproject mysite
    ```
3. Run Django Migrations
    ```python
    python manage.py migrate
    ```
4. Create Admin User
    ```python
    python manage.py createsuperuser
    ```
5. Install Django Rest Framework
    ```python
    pip install djangorestframework
    ```
6. Criate you (business) app with Django
    ```python
    python manage.py startapp myapp
    ```
7. Modeling your (business) tables and generate migrations
    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```