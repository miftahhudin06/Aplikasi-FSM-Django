# Generated by Django 4.0.5 on 2023-07-02 14:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0022_alter_jadwal_tgl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwal',
            name='tgl',
            field=models.DateField(default=datetime.datetime(2023, 7, 2, 14, 22, 50, 959804, tzinfo=utc), null=True),
        ),
    ]