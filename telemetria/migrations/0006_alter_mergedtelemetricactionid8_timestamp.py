# Generated by Django 5.0.1 on 2024-02-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemetria', '0005_alter_mergedtelemetricactionid8_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mergedtelemetricactionid8',
            name='timestamp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]