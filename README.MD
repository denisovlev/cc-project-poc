# Deployment Configuration #
## Vagrant ##
Export the following environment variables. (We can put it in ~/.bashrc file so that it will load every time terminal runs)
```bash
export AWS_ACCESS_KEY='AWS_ACCESSS_KEY'
export AWS_SECRET_KEY='AWS_SECRET_KEY'
export AWS_DEFAULT_REGION='AWS_DEFAULT_REGION'
export AWS_PRIVATE_KEY_PATH='AWS_PRIVATE_KEY_PATH.pem'
export AWS_EC2_KEY_NAME='AWS_EC2_KEY_NAME'
export AWS_SECURITY_GROUP_NAME='AWS_SECURITY_GROUP_NAME'
```

# Python Configuration #
* For development environment (using postgresql): create .env file inside settings directory with content : 
```bash
DBNAME='DBNAME'
DBUSERNAME='DBUSERNAME'
DBPASSWORD='DBPASSWORD'
DBHOST='DBHOST'
DBPORT='DBPORT'
```
* For all environment: create .env file inside settings containing:
```bash
RACO_CLIENT_ID='RACO_CLIENT_ID'
RACO_CLIENT_SECRET='RACO_CLIENT_SECRET'
RACO_AUTH_URL='RACO_AUTH_URL'
```


# How to run #
## Migration ##

* Local: 
```bash
python manage.py makemigrations oauth_poc --settings=settings.local # if needed
python manage.py sqlmigrate oauth_poc 0001 --settings=settings.local # if needed
python manage.py migrate --settings=settings.local
```
* Development: 
```bash
python manage.py makemigrations oauth_poc --settings=settings.dev # if needed
python manage.py sqlmigrate oauth_poc 0001 --settings=settings.dev # if needed
python manage.py migrate --settings=settings.dev

```

## Run server ##
* Local: 
```bash
python manage.py runserver --settings=settings.local
```

* Development:
```bash
python manage.py runserver --settings=settings.dev
```

## Run Celery background jobs ##

In a separate Terminal console, run `redis-server`.

* Development:
```bash
DJANGO_SETTINGS_MODULE=settings.local celery -A raco_reader worker -l info -B
```

* Production:
```bash
DJANGO_SETTINGS_MODULE=settings.dev  celery -A raco_reader worker -l info
DJANGO_SETTINGS_MODULE=settings.dev celery -A raco_reader beat -l info
```
