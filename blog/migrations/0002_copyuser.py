# Generated by Django 4.1 on 2022-09-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Copyuser',
            fields=[
                ('cu_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=80)),
                ('pin', models.IntegerField(default=0)),
            ],
        ),
    ]
