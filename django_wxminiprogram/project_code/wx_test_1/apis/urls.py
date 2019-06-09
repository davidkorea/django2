from django.urls import path
from .views import weather, menu, image

urlpatterns = [
    # path('weather/', weather.weather_app),
    path('weather/', weather.WeatherView.as_view()),
    path('menu/', menu.get_menu),
    # path('image/', image.image),
    # path('imagetext/', image.image_test)
    path('image/', image.ImageView.as_view()),

]