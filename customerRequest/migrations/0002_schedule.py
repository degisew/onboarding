# Generated by Django 4.2.8 on 2023-12-22 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customerRequest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('meeting', 'Meeting'), ('call', 'Call'), ('email', 'Email')], max_length=255)),
                ('due_date', models.DateTimeField()),
                ('summary', models.TextField()),
                ('fee', models.TextField(max_length=255)),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='customerRequest.customerrequest')),
            ],
        ),
    ]
