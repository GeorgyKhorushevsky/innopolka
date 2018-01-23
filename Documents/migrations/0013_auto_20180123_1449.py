# Generated by Django 2.0.1 on 2018-01-23 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0012_auto_20180120_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentcopy',
            name='checked_up_by_whom',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='documentcopy',
            name='date',
            field=models.DateField(default='2018-01-23'),
        ),
        migrations.AlterField(
            model_name='documentcopy',
            name='returning_date',
            field=models.DateField(default='2018-01-23'),
        ),
    ]