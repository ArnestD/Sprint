# Generated by Django 4.2.3 on 2023-08-28 20:26


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longtitude', models.FloatField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'coords',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(blank=True, null=True)),
                ('img', models.BinaryField()),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(blank=True, null=True)),
                ('raw_data', models.JSONField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('beautytitle', models.TextField(blank=True, db_column='beautyTitle', null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('other_titles', models.TextField(blank=True, null=True)),
                ('connect', models.TextField(blank=True, null=True)),
                ('add_time', models.DateTimeField(blank=True, null=True)),
                ('winter', models.TextField(blank=True, null=True)),
                ('summer', models.TextField(blank=True, null=True)),
                ('autumn', models.TextField(blank=True, null=True)),
                ('spring', models.TextField(blank=True, null=True)),
                ('coord', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pereval.coords')),
            ],
            options={
                'db_table': 'pereval_added',
            },
        ),
        migrations.CreateModel(
            name='PerevalAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_parent', models.BigIntegerField()),
                ('title', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pereval_areas',
            },
        ),
        migrations.CreateModel(
            name='SprActivitiesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'spr_activities_types',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=320, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('fam', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('otc', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pereval.images')),
                ('pereval', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pereval.perevaladded')),
            ],
            options={
                'db_table': 'pereval_images',
            },
        ),
    ]
