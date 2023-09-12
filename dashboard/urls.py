from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


app_name = 'dashboard'
urlpatterns=[
    path('',views.DashboardView.as_view(), name='messages'),  
    path('message/<int:pk>/', views.Receivedmsg.as_view(), name='receivedmsg'),
    path('<int:pk>/delete/', views.deletemsg.as_view(), name='deletemsg'),
    path('blogs/', views.BlogView.as_view(), name='blogsview'),
    path('content/<int:pk>/', views.Blogscontent.as_view(), name='blogcontent'),
    path('addBlog/', views.add_blog,name="addblog" ),
    path('<int:pk>/deleteblog/', views.deleteblog.as_view(), name='deleteblog'),
    path('addBlog/<int:pk>/', views.updateblog.as_view(),name="updateblogs" ),
    path('', login_required(views.DashboardView.as_view(), login_url='/admin/login/?next=/admin/')),
    path('logout/', auth_views.LogoutView.as_view(),  name = 'logout'),

]