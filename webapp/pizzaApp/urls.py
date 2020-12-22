from django.urls import path
from . import views

urlpatterns = [
    path('addpizza', views.CreatePizza.as_view()),
    path('getpizza', views.GetPizza.as_view()),
    path('getpizza/pizza_type/<str:pizza_type>', views.GetPizza.as_view()),
    path('getpizza/pizza_size/<str:pizza_size>', views.GetPizza.as_view()),
    path('editpizza/<int:id>', views.EditPizza.as_view())
]