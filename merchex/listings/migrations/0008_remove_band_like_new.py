# Generated by Django 5.1 on 2024-10-05 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_band_like_new_alter_listing_band'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]
