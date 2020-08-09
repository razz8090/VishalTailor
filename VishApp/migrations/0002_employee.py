# Generated by Django 3.0.5 on 2020-07-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VishApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('adhar', models.CharField(max_length=20)),
            ],
        ),
    ]
