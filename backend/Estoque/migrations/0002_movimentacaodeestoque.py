# Generated by Django 4.2.4 on 2023-11-25 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0002_material_fornecedor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimentacaoDeEstoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantidade', models.IntegerField()),
                ('tipo', models.CharField(max_length=30)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiais.material')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
