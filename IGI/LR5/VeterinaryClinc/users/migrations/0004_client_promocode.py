# Generated by Django 4.2.13 on 2024-05-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_doctor_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='promocode',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
