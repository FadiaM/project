# Generated by Django 3.0.3 on 2020-03-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
