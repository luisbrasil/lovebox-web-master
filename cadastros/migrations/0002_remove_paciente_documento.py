# Generated by Django 4.0.4 on 2022-05-31 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='documento',
        ),
    ]