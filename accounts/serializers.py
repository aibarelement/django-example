from rest_framework import serializers
from accounts import models


class _WalletAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = ('id', 'first_name', 'last_name')


class WalletSerializer(serializers.ModelSerializer):
    # account = _WalletAccountSerializer(read_only=True)

    class Meta:
        model = models.Wallet
        fields = '__all__'


class _AccountWalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wallet
        fields = (
            'amount',
            'amount_currency',
        )


class CreateAccountSerializer(serializers.ModelSerializer):
    wallets = _AccountWalletSerializer(write_only=True, many=True)

    class Meta:
        model = models.Account
        fields = '__all__'


class RetrieveAccountSerializer(serializers.ModelSerializer):
    total_amount = serializers.DecimalField(
        max_digits=14, decimal_places=2, read_only=True
    )
    avg_amount = serializers.DecimalField(
        max_digits=14, decimal_places=2, read_only=True
    )
    custom_amount = serializers.DecimalField(
        max_digits=14, decimal_places=2, read_only=True
    )
    wallets = _AccountWalletSerializer(read_only=True, many=True)

    class Meta:
        model = models.Account
        fields = '__all__'


class ListAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = '__all__'
