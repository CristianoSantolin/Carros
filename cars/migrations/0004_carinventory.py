# Generated by Django 5.0.7 on 2024-07-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_photo_car_plate'),
    ]

    operations = [
        migrations.CreateModel(
            name='carInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars_coumt', models.IntegerField()),
                ('cars_value', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
