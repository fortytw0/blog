import json

secrets_file = open("secrets.json")
secrets = json.load(secrets_file)
secrets_file.close()

from django.contrib.sites.models import Site
one = Site.objects.all()[0]
one.domain = secrets['DOMAIN']
one.name = secrets['NAME']
one.save()