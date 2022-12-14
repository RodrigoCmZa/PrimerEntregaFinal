# Generated by Django 4.0.6 on 2022-08-02 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppFamilia', '0003_alter_tareas_options_alter_tareas_dia_de_creacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fechaNacimiento', models.DateField()),
                ('ocupacion', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ('apellido', 'nombre'),
                'unique_together': {('nombre', 'apellido', 'edad', 'fechaNacimiento')},
            },
        ),
        migrations.DeleteModel(
            name='Familia',
        ),
        migrations.AlterModelOptions(
            name='herramientas',
            options={'ordering': ('nombre', 'tipo_de_tarea', 'responsable_de_uso'), 'verbose_name': 'Herramienta', 'verbose_name_plural': 'Herramientas'},
        ),
        migrations.AlterModelOptions(
            name='tareas',
            options={'ordering': ('dia_de_creacion', '-nombre', 'responsable'), 'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
        migrations.RemoveField(
            model_name='tareas',
            name='responsables',
        ),
        migrations.AlterField(
            model_name='herramientas',
            name='tipo_de_tarea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppFamilia.tareas'),
        ),
        migrations.AddField(
            model_name='tareas',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppFamilia.empleados'),
        ),
        migrations.AlterField(
            model_name='herramientas',
            name='responsable_de_uso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppFamilia.empleados'),
        ),
    ]
