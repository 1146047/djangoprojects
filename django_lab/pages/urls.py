from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("hello/<str:name>", views.hello_name, name="hello"),
    path("search/",views.search,name="search"),
    path("catalog/",views.catalog,name="catalog"),
]