from django.urls import path


from . import views


urlpatterns = [
    # basically the home page for restaurants
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('main/', views.main, name='main'),
    path('testing_api/', views.testing_api, name='testing_api'),
    # if we were to render a page that needs a specific id:
    #path('<int:restaurants_id>', views.restaurant, name='restaurant')
]
