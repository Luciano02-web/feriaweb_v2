# Generated by Django 4.0.5 on 2022-11-28 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calzado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('talle', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
        ),
        migrations.CreateModel(
            name='Camisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('talle', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
        ),
        migrations.CreateModel(
            name='Campera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('talle', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
        ),
        migrations.CreateModel(
            name='Jean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('talle', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
        ),
        migrations.CreateModel(
            name='Remera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('talle', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
        ),
        migrations.CreateModel(
            name='Todo100',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('talle', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
        ),
    ]
