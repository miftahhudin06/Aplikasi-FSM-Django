# Generated by Django 4.0.5 on 2023-07-30 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0024_alter_jadwal_tgl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwal',
            name='tgl',
            field=models.DateField(null=True),
        ),
    ]
