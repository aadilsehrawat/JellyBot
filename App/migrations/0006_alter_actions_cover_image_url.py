# Generated by Django 4.2 on 2023-04-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_rename_cover_actions_cover_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='cover_image_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
