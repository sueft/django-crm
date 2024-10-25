from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('create/', views.create, name='create'),
    path('update/<int:product_id>/', views.update, name='update'),
    path('delete/<int:product_id>/', views.delete, name='delete'),
    path('register/',views.register, name="register") 

]