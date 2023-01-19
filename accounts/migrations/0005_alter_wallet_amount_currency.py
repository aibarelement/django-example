# Generated by Django 4.1.4 on 2023-01-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_wallet_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='amount_currency',
            field=models.CharField(choices=[('RUB', 'Rub'), ('KZT', 'Kzt'), ('USD', 'Usd')], default='KZT', max_length=3),
        ),
    ]