# Generated by Django 4.2 on 2023-04-22 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_file', models.FileField(blank=True, null=True, upload_to='input_file/')),
                ('output_file', models.FileField(blank=True, null=True, upload_to='output_file/')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.actions')),
            ],
            options={
                'verbose_name': 'Perform Logs',
                'verbose_name_plural': 'Perform Logs',
            },
        ),
    ]