from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'CIS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^create/', 'careers.views.create', name='create'),
    url(r'^', 'careers.views.home', name='home'),
    
]
