# Generated by Django 3.2.8 on 2021-10-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6),
        ),
    ]