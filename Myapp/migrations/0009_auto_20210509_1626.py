# Generated by Django 3.1.7 on 2021-05-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0008_auto_20210509_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sikk',
            name='symptom1',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='sikk',
            name='symptom2',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='sikk',
            name='symptom3',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='sikk',
            name='symptom4',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='sikk',
            name='symptom5',
            field=models.CharField(max_length=300),
        ),
    ]
