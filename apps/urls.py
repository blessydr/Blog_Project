from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='home'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
]
