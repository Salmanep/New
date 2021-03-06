# Generated by Django 3.1.7 on 2021-05-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_sikk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='id',
        ),
        migrations.RemoveField(
            model_name='doctors',
            name='id',
        ),
        migrations.RemoveField(
            model_name='hospitals',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sikk',
            name='id',
        ),
        migrations.AlterField(
            model_name='disease',
            name='disease',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='doctor',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='hospital',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sikk',
            name='disease',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
