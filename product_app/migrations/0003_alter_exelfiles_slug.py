# Generated by Django 5.0.7 on 2024-08-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_alter_exelfiles_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exelfiles',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=200, unique=True),
        ),
    ]
