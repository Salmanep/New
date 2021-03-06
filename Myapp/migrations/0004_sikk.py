# Generated by Django 3.1.7 on 2021-05-06 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_auto_20210506_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sikk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('cause', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=50)),
                ('symptom1', models.IntegerField()),
                ('symptom2', models.IntegerField()),
                ('symptom3', models.IntegerField()),
                ('symptom4', models.IntegerField()),
                ('symptom5', models.IntegerField()),
                ('symptom6', models.IntegerField()),
                ('symptom7', models.IntegerField()),
                ('symptom8', models.IntegerField()),
                ('symptom9', models.IntegerField()),
                ('symptom10', models.IntegerField()),
                ('symptom11', models.IntegerField()),
                ('symptom12', models.IntegerField()),
                ('symptom13', models.IntegerField()),
                ('symptom14', models.IntegerField()),
                ('symptom15', models.IntegerField()),
                ('symptom16', models.IntegerField()),
                ('symptom17', models.IntegerField()),
                ('symptom18', models.IntegerField()),
                ('symptom19', models.IntegerField()),
                ('symptom20', models.IntegerField()),
                ('symptom21', models.IntegerField()),
                ('symptom22', models.IntegerField()),
                ('symptom23', models.IntegerField()),
            ],
        ),
    ]
