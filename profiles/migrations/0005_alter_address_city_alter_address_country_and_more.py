# Generated by Django 4.0.6 on 2022-11-22 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_address_flat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=30, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=20, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='address',
            name='flat',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='address',
            name='house',
            field=models.CharField(max_length=20, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(max_length=20, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=20, verbose_name='Улица'),
        ),
    ]