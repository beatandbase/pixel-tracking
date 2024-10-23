# Generated by Django 5.1.2 on 2024-10-23 12:00

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_info', models.JSONField()),
                ('location', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='TrackRecord',
            fields=[
                ('tracker_id', models.CharField(default=uuid.uuid4, max_length=60, primary_key=True, serialize=False)),
                ('email_recipient', models.CharField(max_length=250)),
                ('visit_count', models.PositiveSmallIntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]