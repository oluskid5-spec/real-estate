from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("properties/", views.property_list, name="properties"),
    path("property/<int:pk>/", views.property_detail, name="property_detail"),
    path("contact/", views.contact, name="contact"),
]
