from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task4_app.models import User
from django.conf.urls import include
from task4_app.serializers import UserSerializer, GroupSerializer
from task4_app.views import RegisterApi, LoginApi, GroupApi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register("register", RegisterApi, "Register")
router.register("login", LoginApi, "Login")

router.register("group", GroupApi, "Group")






urlpatterns = [
    path("", include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]