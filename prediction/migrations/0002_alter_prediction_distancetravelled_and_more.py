# Generated by Django 4.0.4 on 2022-08-04 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='distanceTravelled',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='engineSize',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='maxPower',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='seatType',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='vehicleAge',
            field=models.IntegerField(default=0),
        ),
    ]
