# Generated by Django 4.0.4 on 2022-06-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0009_cuidador_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuidador',
            name='crc',
            field=models.IntegerField(blank=True, null=True, verbose_name='CRC'),
        ),
        migrations.AlterField(
            model_name='cuidador',
            name='redes_sociais',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Redes Sociais'),
        ),
    ]
