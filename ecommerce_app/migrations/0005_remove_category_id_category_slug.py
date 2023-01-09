# Generated by Django 4.1.5 on 2023-01-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0004_customer_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='-', primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
