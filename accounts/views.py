from rest_framework.viewsets import ModelViewSet
from accounts import serializers, models


class WalletViewSet(ModelViewSet):
    queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletSerializer


class AccountViewSet(ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
