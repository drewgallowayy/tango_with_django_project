# Generated by Django 2.2.3 on 2020-02-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
