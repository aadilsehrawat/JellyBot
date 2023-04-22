# Generated by Django 4.2 on 2023-04-22 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('performed', models.IntegerField(default=0)),
                ('cover', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]