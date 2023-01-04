from django.contrib import admin
from django.urls import path
from prediction.views import PredictionView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prediction/', PredictionView.as_view(), name="prediction"),
]
