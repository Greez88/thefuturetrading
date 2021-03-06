# Generated by Django 3.2.11 on 2022-04-10 20:12

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TradingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_gateway', models.CharField(choices=[('BITCOIN', 'BITCOIN'), ('ETHEREUM', 'ETHEREUM'), ('USDT', 'USDT')], default='Bitcoin', max_length=255)),
                ('amount_in_USD', models.IntegerField()),
                ('wallet_address', models.CharField(default='null', max_length=400)),
                ('withdrawal_status', models.CharField(choices=[('PENDING', 'PENDING'), ('CONFIRMED', 'CONFIRMED')], default='Pending', max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTradingAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('btc_balance_equivalent', models.CharField(blank=True, max_length=255, null=True)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TradingOptionsChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tradingoptions')),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_plan', models.CharField(choices=[('CLASSIC', 'CLASSIC'), ('STANDARD', 'STANDARD'), ('PREMIUM', 'PREMIUM'), ('ULTIMATE', 'ULTIMATE')], default='CLASSIC', max_length=255)),
                ('amount_in_USD', models.IntegerField()),
                ('cryptocurrency', models.CharField(choices=[('BITCOIN', 'BITCOIN')], default='Bitcoin', max_length=255)),
                ('investment_status', models.CharField(choices=[('PENDING', 'PENDING'), ('CONFIRMED', 'CONFIRMED')], default='Pending', max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('postal_code', models.IntegerField()),
                ('account_status', models.CharField(choices=[('NOT VERIFIED', 'NOT VERIFIED'), ('VERIFIED', 'VERIFIED')], default='Not Verified', max_length=255)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='verify', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
