# Generated by Django 4.0.4 on 2022-06-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0014_alter_tratamento_data_prescricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tratamento',
            name='data_prescricao',
            field=models.DateField(),
        ),
    ]