"""
Also see: _urls.old.py
"""
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    # recipes
    # "old": path('recipes/<int:pk>/', views.DetailRecipe.as_view()),
    # "old": path('recipes/', views.ListRecipe.as_view()),
]

router = SimpleRouter()
router.register('blogs', views.BlogViewSet, basename='blogs')
router.register('bookings', views.BookingViewSet, basename='bookings')
router.register('recipes', views.RecipeViewSet, basename='recipes')
router.register('users', views.UserViewSet, basename='users')
urlpatterns = router.urls
