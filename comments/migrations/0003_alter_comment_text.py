# Generated by Django 4.0.6 on 2022-10-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_options_comment_active_comment_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=200, verbose_name='Комментарий'),
        ),
    ]
