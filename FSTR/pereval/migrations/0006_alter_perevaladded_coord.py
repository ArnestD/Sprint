# Generated by Django 4.2.3 on 2023-08-26 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0005_alter_perevaladded_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='coord',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perevals', to='pereval.coords'),
        ),
    ]