# Deals
Create web pages/views Consuming REST API to process the following features:
· Add new user
· Add new deal
· Ability to Change User/Deal Status (Active, In Active, Deleted, Expired)
· Ability to Login for Registered Users and to view all available deals and option to claim the selected deal.
· Grid view of all users saved on the database (Admin Access) (Grid must return 10 records at a time)
· Grid view of all deals saved on the database (Admin Access) (Grid must return 10 records at a time)
· Grid view of all claimed deals saved on the database and search by user id (Admin Access) (Grid must return 10 
records at a time)
· Delete one or more user on the same time (Admin Access)
· Show Count and Total amounts of claimed deals on user profile 
· Upload user Photo and Save it on Database




#
Token Authentication
poetry add 


Django==4.2.1
django-datetime-utc==1.0.4
django-filter==23.2
django-phonenumber-field==7.1.0
djangorestframework==3.14.0
importlib-metadata==6.6.0
Markdown==3.4.3
phonenumbers==8.13.11
Pillow==9.5.0
python-dateutil==2.8.2
pytz==2023.3
six==1.16.0
sqlparse==0.4.4
zipp==3.15.0
PostgreSQL { pip install psycopg2}