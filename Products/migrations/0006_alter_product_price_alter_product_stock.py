# Generated by Django 5.0.6 on 2024-06-29 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_alter_category_decription_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
