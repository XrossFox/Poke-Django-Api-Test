# Generated by Django 3.1.4 on 2020-12-30 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20201230_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='slot_2_dex_id',
            new_name='slot_2_national_dex_id',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='slot_3_dex_id',
            new_name='slot_3_national_dex_id',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='slot_4_dex_id',
            new_name='slot_4_national_dex_id',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='slot_5_dex_id',
            new_name='slot_5_national_dex_id',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='slot_6_dex_id',
            new_name='slot_6_national_dex_id',
        ),
    ]
