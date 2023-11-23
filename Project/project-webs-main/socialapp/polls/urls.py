from django.urls import path
from .views import  signupclass , VericationView, Loginclass,Settingclass,homeclass,uppostclass, logout,profileclass,follow,Likepostclass
from django.contrib.auth.decorators import login_required


app_name= "web"
urlpatterns = [
    path('signup/', signupclass.as_view(), name='signup'),
    path('signin/', Loginclass.as_view(), name='signin'),
    path("upload", uppostclass.as_view(),name="upload"),
    path('like-post', Likepostclass.as_view(), name='like-post'),
    path("logout", logout, name="logout"),
    path("activate/<uidb64>/<token>", VericationView.as_view(), name="activate"),
    path('settings/', login_required(Settingclass.as_view()) , name='settings'),
    path("home", login_required(homeclass.as_view()),name="home"),
    path("upload", uppostclass.as_view(),name="upload"),
    path("profile/<str:pk>", profileclass.as_view(),name="profile"),
    path("follow", follow, name="follow"),
    

]