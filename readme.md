# Project Setup Guide

This Read Me file will guide you through the necessary steps to get the project up and running.

## Prerequisites
Make sure your Python virtual environment contains the necessary packages:
- django = "*"
- mysqlclient = "*"
- djangorestframework = "*"
- djoser = "*"

## Database Configuration
Set your database configuration in the `DATABASES` variable within `settings.py`.

## Migrate Models
Migrate the models to your database using the following commands:
```
python manage.py makemigrations
python manage.py migrate
```

## Run unit test
Run model and view unit tests using the following commands:
```
python manage.py test
```
## Create superuser
If you haven't created any users yet, create at least one using the following command
```
python manage.py createsuperuser
```
Now you can visit the admin page to add more users or create objects

   - URL: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - Description: Django admin homepage.

## Usage

Now you can visit the following URLs assuming your project works on port 8000.

1. **Homepage - Static Files Usage**
   - URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Description: Checkout usage of static files on the homepage.

2. **Menu Items**
   - Read or add new menu items through DRF API.
   - URL: [http://127.0.0.1:8000/api/menu-items/](http://127.0.0.1:8000/api/menu-items/)

3. **Single Menu Item**
   - Read, update, or delete information of a single menu item through DRF API (specify item id).
   - URL: [http://127.0.0.1:8000/api/menu-items/1](http://127.0.0.1:8000/api/menu-items/1)

4. **Bookings**
   - Read or add new bookings through DRF API.
   - URL: [http://127.0.0.1:8000/api/bookings/](http://127.0.0.1:8000/api/bookings/)

5. **Single Booking**
   - Read, update, or delete information of a single booking through DRF API (specify item id).
   - URL: [http://127.0.0.1:8000/api/bookings/1/](http://127.0.0.1:8000/api/bookings/1/)

6. **User Management using Djoser**
   - Read existing users or register a new user.
   - URL: [http://127.0.0.1:8000/auth/users/](http://127.0.0.1:8000/auth/users/)
   - Login with user credentials and get access token 
   - URL: [http://127.0.0.1:8000/auth/token/login](http://127.0.0.1:8000/auth/token/login/)
   - Logout (post auth token you want to destroy)
   - URL: [http://127.0.0.1:8000/auth/token/logout](http://127.0.0.1:8000/auth/token/logout/)

## Important Notes
- Users must be logged in to perform operations through the web interface.
- Users must specify a token when performing operations using an API client like Insomnia.
- Make sure to generate necessary tokens for your users. You can do this either through the admin interface or by using the following URL: [http://127.0.0.1:8000/api/api-token-auth/](http://127.0.0.1:8000/api/api-token-auth/) (using Insomnia or a similar tool).

Feel free to reach out if you encounter any issues or have any questions.