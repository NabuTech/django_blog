# Generated by Django 4.0.8 on 2024-04-18 01:36

from django.db import migrations, models
import nabutech_content.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=nabutech_content.models.upload_location)),
                ('introduction', models.TextField()),
            ],
        ),
    ]
