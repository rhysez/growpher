from django.urls import path
from . import views

# This list contains route definitions, e.g. what to return for each endpoint.
# Using "" references the root segment of our path.
# We then call views.function_name from our views.py file, and assign it a name.
urlpatterns = [
    path("", views.index, name="index"),
]