# Generated by Django 2.2.5 on 2019-10-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='fechaRegistro',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
