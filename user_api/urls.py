from .views import UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'user', UserView, basename='user')

urlpatterns = router.urls
