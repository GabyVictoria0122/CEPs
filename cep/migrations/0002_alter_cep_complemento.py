# Generated by Django 4.0.6 on 2022-07-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cep', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cep',
            name='complemento',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
