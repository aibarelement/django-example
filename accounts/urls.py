from rest_framework.routers import DefaultRouter

from accounts import views


router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet)
router.register(r'wallets', views.WalletViewSet)


urlpatterns = router.urls
