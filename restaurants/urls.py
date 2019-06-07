from django.urls import path


from . import views


urlpatterns = [
    # basically the home page for restaurants
    path('', views.indexer, name='restaurants'),
    path('detail/', views.restaurant_detail, name='restaurant_detail'),
    # if we were to render a page that needs a specific id:
    #path('<int:restaurants_id>', views.restaurant, name='restaurant')
]
