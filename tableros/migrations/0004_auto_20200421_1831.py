# Generated by Django 2.1.15 on 2020-04-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableros', '0003_auto_20200421_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablero',
            name='url',
            field=models.URLField(blank=True, default=''),
        ),
    ]
