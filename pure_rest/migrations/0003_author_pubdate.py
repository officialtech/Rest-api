# Generated by Django 3.2.7 on 2021-09-20 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pure_rest', '0002_rename_authors_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='pubdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
