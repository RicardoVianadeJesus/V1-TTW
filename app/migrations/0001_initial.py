# Generated by Django 4.0 on 2021-12-18 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipamento', models.CharField(max_length=100)),
                ('origem', models.CharField(max_length=100)),
                ('setor', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('manutencao', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('dataSaida', models.CharField(max_length=100)),
            ],
        ),
    ]
