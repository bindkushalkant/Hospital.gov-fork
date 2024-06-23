 from django.urls import path
 from . import views

 urlpatterns = [
     path("", views.index, name="index")
     path('Hospital_App/', include("Hospital_App.urls"))
 ]
