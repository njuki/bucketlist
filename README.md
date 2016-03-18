# Project Description
There are times things we want to do escape our memory. This Django and Django Rest Framework powered app helps the users keep a track of things they want to do and keep memories of so they never forget or miss to do any of them.

#Tools used
The API has been developed using django rest frame. Its detailed documentation has been done using django rest swagger and can be found here:
http://52.88.3.173:8000/docs/

The UI on the other hand is powered by Django generic views and templates `from django.views.generic`

The system runs on postgres database

# Installation
1. Create a python virtual environment by running the command `mkvirtualenv blist`. This automaticall activates the new environment.
2. Install the dependancy packages by running `pip install -r requirements.txt`
3. Change the db configs appropriately in `configuration/settings.py`
3. Run the db migrations and create an admin user
4. Access the web interface using your favorite browser by pasting the instance url on the browser's address bar.

#Demo
http://52.88.3.173:8000
username: admin
password: !23qweASD

# Testing
1. Testing db is set to sqlite for fast performance.
2. Test configuration file is configuration/test.py

Run the following command from the project root folder to run the tests:
`./manage.py test blist_api --settings=configuration.test`
