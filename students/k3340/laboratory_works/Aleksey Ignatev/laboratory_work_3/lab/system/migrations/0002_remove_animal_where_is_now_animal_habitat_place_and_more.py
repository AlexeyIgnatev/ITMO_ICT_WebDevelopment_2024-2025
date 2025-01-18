# Generated by Django 5.1.4 on 2025-01-14 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='where_is_now',
        ),
        migrations.AddField(
            model_name='animal',
            name='habitat_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='system.habitat'),
        ),
        migrations.AddField(
            model_name='animal',
            name='leaser_name',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='worker',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
