# Generated by Django 4.2.4 on 2024-07-07 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0006_remove_colaborador_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='cargo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='colaboradores.cargos'),
        ),
    ]