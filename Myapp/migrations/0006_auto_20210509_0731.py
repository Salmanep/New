# Generated by Django 3.1.7 on 2021-05-09 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0005_auto_20210507_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disease',
            old_name='symptom1',
            new_name='symptoms',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='symptom10',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='symptom2',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='symptom3',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='symptom4',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='symptom5',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='symptom6',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='symptom7',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='symptom8',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='symptom9',
        ),
    ]