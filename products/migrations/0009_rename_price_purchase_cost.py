# Generated by Django 4.0.6 on 2022-11-21 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_purchase_count_purchase_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='price',
            new_name='cost',
        ),
    ]