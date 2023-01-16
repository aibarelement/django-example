
from rest_framework.viewsets import ModelViewSet
from accounts import serializers, models, filters, services


# one to one
# many to one
class WalletViewSet(ModelViewSet):
    queryset = models.Wallet.objects.select_related('account').all()
    serializer_class = serializers.WalletSerializer
    filterset_class = filters.WalletFilter


# many to many
# one to many
class AccountViewSet(ModelViewSet):
    account_services = services.AccountServicesV1()
    serializer_class = serializers.AccountSerializer
    filterset_class = filters.AccountFilter

    def get_queryset(self):
        return self.account_services.get_accounts()

    def perform_create(self, serializer: serializers.AccountSerializer):
        self.account_services.create_account(data=serializer.validated_data)
