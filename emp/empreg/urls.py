from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name='empinsert'),
    path('<int:id>/', views.employee_form, name='empupdate'),
    path('list/', views.employee_list, name='empview'),
    path('delete/<int:id>/', views.employee_delete, name='empdelete')
]
