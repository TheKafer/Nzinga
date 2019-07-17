# Generated by Django 2.2.1 on 2019-07-16 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('iduser', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('iduser', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Info_Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('numberDirectors', models.IntegerField(default=0)),
                ('state', models.BooleanField(default=True)),
                ('idEntity', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Info_Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('director', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Director')),
            ],
        ),
    ]
