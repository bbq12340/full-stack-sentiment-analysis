# Generated by Django 3.2.5 on 2021-08-02 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentAnalysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputtext',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='inputtext',
            name='model_result',
        ),
    ]
