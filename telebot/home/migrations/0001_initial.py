# Generated by Django 3.0.7 on 2021-07-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CowinData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('fee_type', models.CharField(max_length=100)),
                ('capacity', models.CharField(max_length=100)),
                ('available_capacity_dose1', models.IntegerField(default=0)),
                ('available_capacity_dose2', models.IntegerField(default=0)),
                ('fee', models.IntegerField(default=0)),
                ('min_age_limit', models.IntegerField(default=45)),
                ('vaccine', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
