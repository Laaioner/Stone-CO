# Generated by Django 4.2.4 on 2024-03-20 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0003_alter_material_nome'),
        ('pecas', '0004_alter_peca_descrição'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peca',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='materiais.material'),
        ),
    ]