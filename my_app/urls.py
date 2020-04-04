from django.urls import path
from . import views

urlpatterns = [
    # home page '/'
    path('', views.home, name='home'),
    # new_search page '/new_search'
    path('new_search', views.new_search, name='new_search'),
]
