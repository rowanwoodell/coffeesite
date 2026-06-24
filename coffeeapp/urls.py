from django.urls import path

from . import views

app_name = "coffeeapp" \
""
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("new/", views.new_coffee, name="new_coffee"),
    path("<int:pk>/", views.CoffeeDetailView.as_view(), name="coffee_detail")
]
