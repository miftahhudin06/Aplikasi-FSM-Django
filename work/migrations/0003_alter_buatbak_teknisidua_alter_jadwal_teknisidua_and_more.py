# Generated by Django 4.0.5 on 2023-05-06 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_alter_buatbak_teknisisatu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buatbak',
            name='teknisiDua',
            field=models.ForeignKey(limit_choices_to={'is_teknisi': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teknisi2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jadwal',
            name='teknisiDua',
            field=models.ForeignKey(limit_choices_to={'is_teknisi': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pekerja2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jadwal',
            name='teknisiSatu',
            field=models.ForeignKey(limit_choices_to={'is_teknisi': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pekerja1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='picDua',
            field=models.ForeignKey(limit_choices_to={'is_teknisi': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pic2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='picSatu',
            field=models.ForeignKey(limit_choices_to={'is_teknisi': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pic1', to=settings.AUTH_USER_MODEL),
        ),
    ]
