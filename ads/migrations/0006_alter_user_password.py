# Generated by Django 4.1.3 on 2022-11-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
