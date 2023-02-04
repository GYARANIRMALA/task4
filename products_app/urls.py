from django.urls import path, include
from task4_app.models import User
from rest_framework.routers import DefaultRouter
from products_app.models import Product
from products_app.serializers import ProductSerializer
from products_app.views import ProductApi


router = DefaultRouter()
router.register("product", ProductApi, "Product")


urlpatterns = [
    path("", include(router.urls)),
]