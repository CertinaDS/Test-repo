# Generated by Django 4.2.17 on 2025-06-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=13),
        ),
    ]
