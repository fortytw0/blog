from django.urls import path
from concordancer.views import reddit_auth_redirect, concordancer_base

app_name = 'concordancer'

urlpatterns = [
    path('', concordancer_base, name='concordancer_base' ),
    # path('reddit-auth/', reddit_auth_redirect, name='reddit_auth_redirect')
]