# Generated by Django 3.2.16 on 2022-10-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20221025_0847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprestimo',
            options={'ordering': ['data_atualizacao'], 'verbose_name': 'Emprestimo', 'verbose_name_plural': 'Emprestimos'},
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]