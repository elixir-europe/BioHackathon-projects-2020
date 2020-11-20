`docker-compose up --build` 
`docker exec -it app_web_1 /bin/bash`
You are now in the docker container's shell, you should be in /code, then you can do: `cd django`, `python manage.py createsuperuser` to create a user for the admin interface

Go to localhost/admin to get the admin UI, you can log in with the super user details

You can do `python manage.py shell` to enter the Django shell and e.g. do db queries easily, see https://docs.djangoproject.com/en/3.1/intro/tutorial02/
