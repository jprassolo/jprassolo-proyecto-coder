# Generated by Django 4.2.5 on 2023-09-11 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPortfolioTracker', '0005_crypto_alter_activos_act_moneda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bon_ticker', models.CharField(max_length=4)),
                ('bon_nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
