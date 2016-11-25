from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from accounts import views


# Create a router and register our viewsets with it
router = DefaultRouter()
# router.register(r'register', views.RegisterViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/$', views.RegisterViewSet.as_view(), name='register'),
]
