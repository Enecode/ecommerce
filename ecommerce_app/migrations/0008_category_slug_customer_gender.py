# Generated by Django 4.1.5 on 2023-01-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0007_remove_customer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(default='-', max_length=2),
            preserve_default=False,
        ),
    ]