# Generated by Django 4.0.6 on 2022-10-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='hand_tool',
        ),
        migrations.RemoveField(
            model_name='category',
            name='household_tool',
        ),
        migrations.RemoveField(
            model_name='category',
            name='power_tool',
        ),
        migrations.AddField(
            model_name='category',
            name='product_category',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Категория товара'),
        ),
        migrations.AlterField(
            model_name='status',
            name='availability',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Наличие'),
        ),
    ]
