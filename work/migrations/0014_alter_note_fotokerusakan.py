# Generated by Django 4.0.5 on 2023-06-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0013_alter_note_bulan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='fotoKerusakan',
            field=models.CharField(max_length=100, null=True),
        ),
    ]