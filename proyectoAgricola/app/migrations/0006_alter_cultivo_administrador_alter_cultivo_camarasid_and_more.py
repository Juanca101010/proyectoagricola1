# Generated by Django 4.1.1 on 2022-11-02 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_administrador_cultivos_cultivo_administrador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivo',
            name='administrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='administrador', to='app.administrador'),
        ),
        migrations.AlterField(
            model_name='cultivo',
            name='camarasid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='camaras', to='app.camaras'),
        ),
        migrations.AlterField(
            model_name='cultivo',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='cultivo',
            name='localidad',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='cultivo',
            name='sensorhumedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sensor_humedad', to='app.sensorhumedad'),
        ),
        migrations.AlterField(
            model_name='cultivo',
            name='sensortemperatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sensor_temperatura', to='app.sensortemperatura'),
        ),
    ]