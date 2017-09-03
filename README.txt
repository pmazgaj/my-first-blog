Summary:
Python version 3.52, Django 1.11

How to run:
In main project folder (ims_site, where manage.py is located) run:
python manage.py runserver

Get all posts from api:
http://127.0.0.1:8000/api/shop/

Get specific post from api:
http://127.0.0.1:8000/api/shop/<shop_number>/

Edit specific shop:
http://127.0.0.1:8000/shop/<shop_number>/edit

See specific shop:
http://127.0.0.1:8000/shop/<shop_number>/

Create shop:
http://127.0.0.1:8000/shop/<shop_number>/create

Delete specific shop <shop_number>:
http://127.0.0.1:8000/shop/<shop_number>/delete

Command to import to admin (from csv, not working yet)
NOTE: First - comment out, which model you want to fill

Type: python import.py into cmd (in folder)
