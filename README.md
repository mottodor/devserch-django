# Devsearch

Create your profile, add projects and get feedback

# Pre-Requisites

-   Python 3.10.2
-   Virtualenv
-   Git

# Steps to run:

-   Clone the project using the command "git clone https://github.com/mottodor/devserch-django.git"
-   Run "virtualenv .venv"
-   Activate virtual env
-   pip install requirements.txt
-   Run "python manager.py makemigrations"
-   Run "python manager.py migrate"
-   Run "python manager.py createsuperuser"
-   Run "python manage.py runserver" to start the server

# Additional changes

-   Edit settings.py for mailing feature
-   Delete comments from users/signals.py
