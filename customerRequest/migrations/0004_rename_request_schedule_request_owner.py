# Generated by Django 4.2.8 on 2023-12-22 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerRequest', '0003_alter_schedule_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='request',
            new_name='request_owner',
        ),
    ]