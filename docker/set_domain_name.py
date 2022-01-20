import os
from django.contrib.sites.models import Site

one = Site.objects.all()[0]
one.domain = os.environ.get('DOMAIN')
one.name = os.environ.get('NAME')
one.save()