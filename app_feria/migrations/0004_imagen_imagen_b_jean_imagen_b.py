# Generated by Django 4.0.5 on 2022-11-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_feria', '0003_invernal'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='imagen_b',
            field=models.ImageField(blank=True, null=True, upload_to='avatares_B'),
        ),
        migrations.AddField(
            model_name='jean',
            name='imagen_b',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
