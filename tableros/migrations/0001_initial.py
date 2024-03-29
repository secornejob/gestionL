# Generated by Django 2.1.15 on 2020-04-21 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Tablero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tableros.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Tableros',
                'ordering': ['categoria', 'nombre'],
            },
        ),
    ]
