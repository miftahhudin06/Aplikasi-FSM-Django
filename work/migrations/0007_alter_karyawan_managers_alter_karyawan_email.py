# Generated by Django 4.0.5 on 2023-05-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_alter_karyawan_foto'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='karyawan',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='karyawan',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
