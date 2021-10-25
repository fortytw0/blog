from django.contrib import admin
from django.urls import path, include

import config.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.default_view, name='default'),
    path('blogs/<slug:slug>', views.blog_view, name='blog'), 
    path('blogs/', views.blog_list_view, name='blog_list'),
    # path('concordancer/', include('concordancer.urls'))   
] 


