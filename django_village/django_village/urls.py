"""django_village URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from todo.views import index, delete, update, mark_complete

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('mark_complete/<int:todo_id>/', mark_complete, name='mark_complete'),
    path('delete/<int:todo_id>/', delete, name='delete'),
    path('update/<int:todo_id>/', update, name='update'),
    path('post_update/<int:todo_id>/', update, name='post_update'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)