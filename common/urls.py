from django.urls import include, path
from rest_framework import routers
from common.views import BlogViewSet, login, register


router = routers.DefaultRouter()

router.register("blogs",BlogViewSet,basename="blogs")


urlpatterns = [
    path("",include(router.urls)),
    path("login",login),
    path("register",register),
]