from django.urls import path
from . import views
urlpatterns=[path("dealers/",views.dealers),path("dealers/<int:id>/",views.dealer_detail),path("dealers/<int:id>/reviews/",views.reviews),path("carmakes/",views.makes)]
