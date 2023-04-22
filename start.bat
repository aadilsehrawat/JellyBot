@echo off

echo Running makemigrations...
python manage.py makemigrations

echo Running migrate...
python manage.py migrate

echo Starting Django development server...
python manage.py runserver 0.0.0.0:8000

@REM Run this file to start the Django development server by typing "./start.bat" in the command line while in the project directory.