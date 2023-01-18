# Generated by Django 4.1.5 on 2023-01-17 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_apps', '0011_alter_customer_options_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
