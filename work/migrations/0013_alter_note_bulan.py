# Generated by Django 4.0.5 on 2023-06-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0012_alter_note_bulan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='bulan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
