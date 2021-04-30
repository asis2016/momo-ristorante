from django.urls import path

from . import views

urlpatterns = [
    # blog
    path('blogs/', views.ListBlog.as_view()),
    path('blogs/<int:pk>/', views.DetailBlog.as_view()),

    # booking
    path('bookings/', views.ListBooking.as_view()),
    path('bookings/<int:pk>/', views.DetailBooking.as_view()),

    # recipes
    path('recipes/<int:pk>/', views.DetailRecipe.as_view()),
    path('recipes/', views.ListRecipe.as_view()),

    # users
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view())
]
