# Generated by Django 4.2.13 on 2024-09-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
