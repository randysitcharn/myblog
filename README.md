#install all dependencies
$ pip install -r requirements.txt

#runserver local
$ python manage.py migrate --settings=myblog.settings_local
$ python manage.py makemigration --settings=myblog.settings_local
$ python manage.py runserver --settings=myblog.settings_local

#user, pwd
admin, password
