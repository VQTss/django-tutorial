from django.urls  import path
from . import views

urlpatterns = [
    path('', views.index),
    path("test-product/", views.test_product , name="test product")
]





