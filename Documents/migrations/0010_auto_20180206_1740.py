# Generated by Django 2.0.1 on 2018-02-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0009_auto_20180206_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentcopy',
            name='date',
            field=models.DateTimeField(default='2018-02-06 17:40'),
        ),
        migrations.AlterField(
            model_name='documentcopy',
            name='returning_date',
            field=models.DateTimeField(default='2018-02-06 17:40'),
        ),
    ]