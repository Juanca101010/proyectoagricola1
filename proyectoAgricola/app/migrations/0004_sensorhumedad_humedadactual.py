# Generated by Django 4.1.1 on 2022-10-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_cultivo_camarasid_alter_cultivo_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorhumedad',
            name='humedadactual',
            field=models.IntegerField(null=True),
        ),
    ]
