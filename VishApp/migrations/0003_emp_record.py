# Generated by Django 3.0.5 on 2020-07-27 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VishApp', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp_Record',
            fields=[
                ('emp_id', models.IntegerField()),
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('pant', models.IntegerField()),
                ('shirt', models.IntegerField()),
                ('stepend', models.IntegerField()),
            ],
        ),
    ]
