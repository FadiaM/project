# Generated by Django 3.0.3 on 2020-03-25 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_auto_20200321_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='myclubuser',
            name='password1',
            field=models.CharField(max_length=20, null=True, verbose_name='Password'),
        ),
        migrations.AddField(
            model_name='myclubuser',
            name='password2',
            field=models.CharField(max_length=20, null=True, verbose_name='Password confirmation'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]