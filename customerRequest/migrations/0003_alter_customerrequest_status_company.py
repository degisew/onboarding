# Generated by Django 4.2.8 on 2023-12-20 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customerRequest', '0002_customerrequest_status_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrequest',
            name='status',
            field=models.CharField(default='Initiation', max_length=255),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(choices=[('ETH', 'Ethiopia')], max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('tin_number', models.IntegerField()),
                ('business_classification', models.CharField(max_length=255)),
                ('industry', models.TextField(choices=[('IT', 'Information Technology'), ('finance', 'Finance'), ('healthcare', 'Healthcare'), ('business', 'Business')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
