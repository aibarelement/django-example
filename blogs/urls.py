from rest_framework.routers import DefaultRouter

from blogs import views


router = DefaultRouter()
router.register(r'', views.BlogViewSet, basename='blogs')


urlpatterns = router.urls
