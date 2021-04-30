"""
Also see: _urls.old.py
"""
from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    # blog
    path('blogs/', views.BlogList.as_view()),
    path('blogs/<int:pk>/', views.BlogDetail.as_view()),

    # booking
    path('bookings/', views.ListBooking.as_view()),
    path('bookings/<int:pk>/', views.DetailBooking.as_view()),

    # recipes
    path('recipes/<int:pk>/', views.DetailRecipe.as_view()),
    path('recipes/', views.ListRecipe.as_view()),

    # users
    # "old": path('users/', views.UserList.as_view()),
    # "old": path('users/<int:pk>', views.UserDetail.as_view())
]

router = SimpleRouter()
router.register('users', views.UserViewSet, basename='users')
urlpatterns = router.urls

