# Generated by Django 3.2.16 on 2022-10-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_emprestimo_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
