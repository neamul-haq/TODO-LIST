# Generated by Django 4.2.3 on 2023-09-12 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=250)),
                ('Status', models.CharField(choices=[('Complete', 'Complete'), ('In-Complete', 'In-Complete')], max_length=50)),
            ],
        ),
    ]