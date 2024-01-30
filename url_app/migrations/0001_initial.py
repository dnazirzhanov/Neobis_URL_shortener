# Generated by Django 5.0.1 on 2024-01-30 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=20)),
                ('long_url', models.URLField(verbose_name='URL')),
            ],
        ),
    ]
