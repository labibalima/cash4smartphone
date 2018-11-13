# Generated by Django 2.1.2 on 2018-11-11 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20181111_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='internal_memory',
            field=models.CharField(choices=[('16', '16 GB'), ('32', '32 GB'), ('64', '64 GB'), ('128', '128 GB'), ('256', '256 GB')], max_length=3),
        ),
    ]