from django.contrib import admin
from django.urls import path, include

from {{ project_name }}.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.home, name='home'),
]
