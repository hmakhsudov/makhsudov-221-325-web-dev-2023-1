# Generated by Django 4.2.2 on 2023-06-25 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtyapp', '0005_apartment_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='area',
            field=models.FloatField(verbose_name='Площадь'),
        ),
    ]