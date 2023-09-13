# Generated by Django 4.2.5 on 2023-09-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPortfolioTracker', '0004_activos_act_mercado_activos_act_moneda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cry_ticker', models.CharField(max_length=4)),
                ('cry_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='activos',
            name='act_moneda',
            field=models.CharField(default='', max_length=3),
        ),
    ]
