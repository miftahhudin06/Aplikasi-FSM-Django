# Generated by Django 4.0.5 on 2023-06-18 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0014_alter_note_fotokerusakan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buatbak',
            name='fotoKerusakan',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='buatbak',
            name='tgl',
            field=models.DateField(null=True),
        ),
    ]
