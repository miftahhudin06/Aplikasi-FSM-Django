# Generated by Django 4.0.5 on 2023-06-17 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0008_alter_note_tipegondola'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='fotoKerusakan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]