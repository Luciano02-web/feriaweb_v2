# Generated by Django 4.0.5 on 2022-12-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_feria', '0010_alter_jean_genero_alter_jean_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jean',
            name='genero',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], default='Mujer', max_length=50),
        ),
        migrations.AlterField(
            model_name='jean',
            name='talle',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Talle'),
        ),
    ]
