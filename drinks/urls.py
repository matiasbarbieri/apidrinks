from django.contrib import admin
from django.urls import path
from drinks import views
from drinks.models import Drink

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/', views.drink_list),
    path('drinks/<int:pk>/', views.drink_detail),

    
]
