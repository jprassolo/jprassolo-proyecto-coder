# Generated by Django 4.2.5 on 2023-09-14 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appPortfolioTracker', '0006_bonos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activos',
            old_name='act_nombre',
            new_name='act_descripcion',
        ),
        migrations.RenameField(
            model_name='bonos',
            old_name='bon_nombre',
            new_name='bon_descripcion',
        ),
        migrations.RenameField(
            model_name='crypto',
            old_name='cry_nombre',
            new_name='cry_descripcion',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='descripcion',
            new_name='prt_descripcion',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='nombre',
            new_name='prt_nombre',
        ),
    ]
