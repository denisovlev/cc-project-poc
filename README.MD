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
* Create .env file inside root directory with following values (DBHOST will be handled by provisioning): 
```bash
RACO_CLIENT_ID='RACO_CLIENT_ID'
RACO_CLIENT_SECRET='RACO_CLIENT_SECRET'
RACO_AUTH_URL='RACO_AUTH_URL'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='raconotifications@gmail.com'
EMAIL_HOST_PASSWORD='EMAIL_HOST_PASSWORD'
AWS_ACCESS_KEY='AWS_ACCESS_KEY'
AWS_SECRET_KEY='AWS_SECRET_KEY'
AWS_DEFAULT_REGION='AWS_DEFAULT_REGION'
AWS_PRIVATE_KEY_PATH='AWS_PRIVATE_KEY_PATH'
AWS_EC2_KEY_NAME='AWS_EC2_KEY_NAME'
AWS_SECURITY_GROUP_NAME='AWS_SECURITY_GROUP_NAME'
DBNAME='DBNAME'
DBUSERNAME='DBUSERNAME'
DBPASSWORD='DBPASSWORD'
DBHOST='172.31.19.211'
DBPORT=5432
```

# How to run #

## Vagrant ##
In order to make sure that instances are created in the right order, we will sequentially bring them up one by one (db first, and the others later).
It is bundled in script: execute_vagrant.sh.
```
export $(cat .env | xargs) && ./execute_vagrant.sh 

```

## Migration ##

* Development: 
```bash
python manage.py makemigrations oauth_poc --settings=settings.dev # if needed
python manage.py sqlmigrate oauth_poc 0001 --settings=settings.dev # if needed
python manage.py migrate --settings=settings.dev
```
* Production: 
```bash
python manage.py makemigrations oauth_poc --settings=settings.prod # if needed
python manage.py sqlmigrate oauth_poc 0001 --settings=settings.prod # if needed
python manage.py migrate --settings=settings.prod

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

### Racó Reader ###

_This background jobs reads the notifications from Racó and stores the new ones._

In a separate Terminal console, run `redis-server`.

* Development:
```bash
DJANGO_SETTINGS_MODULE=settings.dev celery -A raco_reader worker -l info -B
```

* Production:
```bash
DJANGO_SETTINGS_MODULE=settings.prod  celery -A raco_reader worker -l info
DJANGO_SETTINGS_MODULE=settings.prod celery -A raco_reader beat -l info
```

### Mailer Job ###

_This background jobs sends an email to the user for each new notification. The content of the email is the notification itself._

In a separate Terminal console, run `redis-server`.

* Development:
```bash
DJANGO_SETTINGS_MODULE=settings.dev celery -A mailer_job worker -l info -B
```

* Production:
```bash
DJANGO_SETTINGS_MODULE=settings.prod  celery -A mailer_job worker -l info
DJANGO_SETTINGS_MODULE=settings.prod celery -A mailer_job beat -l info
```
