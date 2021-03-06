# Generated by Django 3.2.5 on 2021-07-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_text', models.TextField(max_length=1000)),
                ('input_time', models.DateTimeField(auto_now_add=True)),
                ('model_result', models.CharField(max_length=10)),
                ('feedback', models.BooleanField()),
            ],
        ),
    ]
