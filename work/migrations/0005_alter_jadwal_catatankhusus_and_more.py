# Generated by Django 4.0.5 on 2023-05-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_alter_jadwal_catatankhusus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwal',
            name='catatanKhusus',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jadwal',
            name='hasilPekerjaan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]