from django.urls import path
from .import views
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

]