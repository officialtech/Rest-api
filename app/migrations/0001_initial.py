# Generated by Django 3.1.7 on 2021-03-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('language', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=5)),
            ],
        ),
    ]