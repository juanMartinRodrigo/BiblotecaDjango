# Generated by Django 3.0.6 on 2020-06-11 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('apellido', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacion', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('apellido', models.CharField(default='', max_length=50)),
                ('direccion', models.CharField(default='', max_length=100)),
                ('telefono', models.CharField(default='', max_length=20)),
                ('ejemplar', models.ManyToManyField(to='proyecto.Ejemplar')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=50)),
                ('editorial', models.CharField(default='', max_length=50)),
                ('paginas', models.IntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Autor')),
            ],
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Libro'),
        ),
    ]
