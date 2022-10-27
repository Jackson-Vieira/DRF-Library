# Generated by Django 3.2.16 on 2022-10-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20221023_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprestimo',
            options={'ordering': ['-data_atualizacao'], 'verbose_name': 'Emprestimo', 'verbose_name_plural': 'Emprestimos'},
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='data_atualizacao',
            field=models.DateField(auto_now=True),
        ),
    ]
