# Generated by Django 2.2.6 on 2019-11-08 00:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('mothersName', models.CharField(max_length=100)),
                ('fathersName', models.CharField(max_length=100)),
                ('contactNumberM', models.CharField(max_length=100)),
                ('contactNumberF', models.CharField(max_length=100)),
                ('pediaName', models.CharField(max_length=100)),
                ('history', models.CharField(max_length=100)),
                ('diagnosis', models.CharField(max_length=100)),
                ('payment', models.IntegerField()),
                ('therapyType', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('SSS', models.CharField(max_length=200)),
                ('TIN', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('week', models.IntegerField()),
                ('month', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('tasks', models.CharField(max_length=500)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('present', models.BooleanField(default=False)),
                ('ref', models.CharField(max_length=200)),
                ('service', models.CharField(max_length=200)),
                ('paid', models.IntegerField()),
                ('schedule', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicapp.Clients')),
            ],
        ),
    ]
