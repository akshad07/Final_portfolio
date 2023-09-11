from django.urls import path
from .views import index, HomePageView 
from . import views
app_name = 'website'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('singleblog/<int:pk>', views.singleblog.as_view(), name='singleblogs'),
    path('login/', views.login_page, name='loginpage'),


]
