from django.urls import path
from . import views

urlpatterns = [
    path('doctors_schedule/', views.doctors_schedule, name="doctors_schedule"),
    path('order_create/', views.order_create, name='order_create'),
    path('orders', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/<int:pk>/update/', views.order_update, name='order_update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),

    path('<int:pk>/', views.service_detail, name='service_detail'),
    path('create/', views.service_create, name='service_create'),
    path('', views.service_list, name='service_list'),
    path('<int:pk>/update/', views.service_update, name='service_update'),
    path('<int:pk>/delete/', views.service_delete, name='service_delete'),
]