from django.urls import path
from . import views

urlpatterns =[
    path('',  views.getData),
    path('add/', views.addItem),
    path('<int:pk>/', views.getItem),
    path('student/<int:pk>/', views.getStudent),
    path('addStd/', views.addStudent),
]