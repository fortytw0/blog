import django
import os
import json

secrets_file = open("secrets.json")
secrets = json.load(secrets_file)
secrets_file.close()

if secrets_file["DJANGO-SECRET-KEY"].strip() == "" : 
    from django.core.management.utils import get_random_secret_key
    os.environ["SECRET_KEY"] = get_random_secret_key()
else : 
    os.environ["SECRET_KEY"] = secrets_file["DJANGO-SECRET-KEY"]

os.environ["DEBUG"] = secrets_file["DEBUG"]

os.environ["ALLOWED-HOSTS"] = secrets_file["ALLOWED-HOSTS"]







