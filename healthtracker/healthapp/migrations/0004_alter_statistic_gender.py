# Generated by Django 3.2.8 on 2021-10-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0003_alter_statistic_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=9),
        ),
    ]