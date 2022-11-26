from django.urls import path
from restaurant.views import RestaurantList, RestaurantDetail, RestaurantSelectList

urlpatterns = [
    path('', RestaurantList.as_view()),
    path('select/', RestaurantSelectList.as_view()),
    path('<str:ext_id>/', RestaurantDetail.as_view()),
]
