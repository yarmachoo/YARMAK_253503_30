# Generated by Django 4.2.13 on 2024-05-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_doctor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='users/%Y/%m/%d/', verbose_name='Фотография'),
        ),
    ]
