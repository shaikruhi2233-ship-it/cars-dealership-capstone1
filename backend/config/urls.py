from django.contrib import admin
from django.urls import path,include
from dealerships import views
urlpatterns=[path("admin/",admin.site.urls),path("api/",include("dealerships.urls")),path("api/auth/register/",views.register),path("api/auth/login/",views.login_view),path("api/auth/logout/",views.logout_view),path("api/sentiment/",views.sentiment)]
