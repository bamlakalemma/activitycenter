# Generated by Django 5.1.1 on 2025-02-07 13:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clubactivity',
            old_name='status',
            new_name='approval_status',
        ),
        migrations.RenameField(
            model_name='clubactivity',
            old_name='description',
            new_name='needs',
        ),
        migrations.AddField(
            model_name='clubactivity',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clubactivity',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='activity_images/'),
        ),
        migrations.AddField(
            model_name='clubactivity',
            name='participants',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clubactivity',
            name='supporting_documents',
            field=models.FileField(blank=True, null=True, upload_to='activity_documents/'),
        ),
        migrations.AddField(
            model_name='clubactivity',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='clubactivity',
            name='transportation_request',
            field=models.BooleanField(default=False),
        ),
    ]
