# Generated by Django 4.2.3 on 2023-08-25 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0004_alter_perevaladded_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='title',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]