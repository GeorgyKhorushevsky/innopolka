# Generated by Django 2.0.1 on 2018-01-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0020_auto_20180126_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentcopy',
            name='date',
            field=models.DateTimeField(default='2018-01-27 20:20'),
        ),
        migrations.AlterField(
            model_name='documentcopy',
            name='returning_date',
            field=models.DateTimeField(default='2018-01-27 20:20'),
        ),
    ]