from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('listall',views.listall, name="listall"),
    path('delete/<int:id>', views.deleterecord, name="deleterecord"),
    path('search',views.search, name="search"),
]
