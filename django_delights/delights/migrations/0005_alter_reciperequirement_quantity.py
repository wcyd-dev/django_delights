# Generated by Django 5.1.3 on 2024-11-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delights', '0004_alter_ingredient_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
