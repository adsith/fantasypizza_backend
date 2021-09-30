from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ingridient/', views.get_ingridients, name='ingridients'),
    path('ingridient/<int:ingredient_id>', views.get_ingridient, name='ingridient')
]
