from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.urls import path

from blogs import views as blog_views
from bookings import views as booking_views
from recipes import views as recipe_views
from . import views

urlpatterns = [
    path('', views.index, name='admin_url_dashboard'),

    # blog
    path('blog', blog_views.BlogListView.as_view(), name='admin_blog'),
    path('blog/create', blog_views.create, name='admin_url_blog_create'),
    path('blog/<int:pk>', blog_views.BlogDetailView.as_view(), name='admin_blog_detail'),
    path('blog/<int:pk>/edit/', blog_views.BlogUpdateView.as_view(), name='admin_blog_update'),
    path('blog/<int:pk>/delete/', blog_views.BlogDeleteView.as_view(), name='admin_blog_delete'),

    # booking
    path('bookings.html', booking_views.BookingListView.as_view(), name='admin_bookings'),
    path('booking/<int:pk>/', booking_views.BookingDetailView.as_view(), name='admin_booking_detail'),

    # recipe
    path('recipes.html', recipe_views.RecipeListView.as_view(), name='admin_recipes'),

    url(r'logout$',
        LogoutView.as_view(),
        name='dashboard_logout'
        ),

    path('endpoints.html', views.endpoints, name='admin_url_endpoints')

]
