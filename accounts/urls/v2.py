from rest_framework.routers import DefaultRouter

from accounts import views


router = DefaultRouter()
router.register(r'accounts', views.AccountViewSetV2, basename='accounts')
router.register(r'wallets', views.WalletViewSet, basename='wallets')


urlpatterns = router.urls
