# Generated by Django 4.2.3 on 2023-08-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0008_images_pereval_delete_perevalimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]