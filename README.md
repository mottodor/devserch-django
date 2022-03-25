# Devsearch 
Create your profile, add projects and get feedback

# Pre-Requisites
- Python 3.10.2
- Poetry
- Git

# Steps to run:
- Clone the project using the command "git clone https://github.com/mottodor/devserch-django.git"
- Run the command "poetry install"
- Run "python manager.py makemigrations"
- Run "python manager.py migrate"
- Run "python manager.py createsuperuser"
- Run "python manage.py runserver" to start the server


# Additional changes 
- Edit settings.py for mailing feature
- Delete commets from users/signals.py 