from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='home'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('create_blog',views.create_blog,name='create' ),
    path('blog_details/<int:pk>/',views.blog_details,name='blog_details' ),

]
