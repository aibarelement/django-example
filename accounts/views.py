from rest_framework.viewsets import ModelViewSet
from accounts import serializers, models, filters


# one to one
# many to one
class WalletViewSet(ModelViewSet):
    queryset = models.Wallet.objects.select_related('account').all()
    serializer_class = serializers.WalletSerializer
    filterset_class = filters.WalletFilter


# many to many
# one to many
class AccountViewSet(ModelViewSet):
    queryset = models.Account.objects.prefetch_related('wallets').all()
    serializer_class = serializers.AccountSerializer
    filterset_class = filters.AccountFilter
