from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import config.views as views

# print(settings.STATIC_URL)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.default_view, name='default'),
    path('blogs/<slug:slug>', views.blog_view, name='blog'), 
    path('blogs/', views.blog_list_view, name='blog_list'),
    path('tags/', views.tag_list_view, name='tag_list'),
    path('tags/<slug:tag>', views.tag_view, name='tag')   

] 

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

