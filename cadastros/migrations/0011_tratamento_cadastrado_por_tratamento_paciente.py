# Generated by Django 4.0.4 on 2022-06-09 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0010_alter_cuidador_crc_alter_cuidador_redes_sociais'),
    ]

    operations = [
        migrations.AddField(
            model_name='tratamento',
            name='cadastrado_por',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='cadastrado_por', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tratamento',
            name='paciente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='paciente_tratemento', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]