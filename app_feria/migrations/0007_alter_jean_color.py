# Generated by Django 4.0.5 on 2022-12-01 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_feria', '0006_alter_jean_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jean',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
