# Generated by Django 4.1.7 on 2023-03-25 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['name']},
        ),
    ]
