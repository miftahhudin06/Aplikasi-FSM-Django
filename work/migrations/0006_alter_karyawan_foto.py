# Generated by Django 4.0.5 on 2023-05-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_alter_jadwal_catatankhusus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karyawan',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='profil_images'),
        ),
    ]