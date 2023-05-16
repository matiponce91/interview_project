from django.urls import path
from . import views

app_name = "urls"
urlpatterns = [
    path('', views.IndexView.as_view(template_name="urls/index.html"), name="index"),
    path('<int:pk>', views.UrlView.as_view(template_name="urls/index.html"), name="url"),
]
