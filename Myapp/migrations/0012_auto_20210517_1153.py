# Generated by Django 3.1.7 on 2021-05-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0011_auto_20210509_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('district', models.CharField(max_length=30)),
                ('hospital', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('photo', models.FileField(upload_to='')),
                ('details', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('emergency', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Cold',
        ),
        migrations.DeleteModel(
            name='Hospitals',
        ),
    ]
