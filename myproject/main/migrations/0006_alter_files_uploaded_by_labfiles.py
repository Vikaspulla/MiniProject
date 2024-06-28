# Generated by Django 5.0.6 on 2024-06-21 05:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_files_uploaded_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Labfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testtype', models.CharField(max_length=20)),
                ('lab_file', models.FileField(upload_to='pdfs/')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('uploaded_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_labfiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]