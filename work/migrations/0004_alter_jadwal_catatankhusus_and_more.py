# Generated by Django 4.0.5 on 2023-05-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_alter_buatbak_teknisidua_alter_jadwal_teknisidua_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwal',
            name='catatanKhusus',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jadwal',
            name='hasilPekerjaan',
            field=models.CharField(max_length=100, null=True),
        ),
    ]