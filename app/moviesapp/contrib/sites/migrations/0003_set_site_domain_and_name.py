# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import migrations


def update_site_forward(apps, schema_editor):
    """Set site domain and name."""
    Site = apps.get_model('sites', 'Site')
    Site.objects.update_or_create(
        id=settings.SITE_ID,
        defaults={
            'domain': 'moviesapp.dev',
            'name': 'Movies CRUD Application'
        }
    )


def update_site_backward(apps, schema_editor):
    """Revert site domain and name to default."""
    Site = apps.get_model('sites', 'Site')
    Site.objects.update_or_create(
        id=settings.SITE_ID,
        defaults={
            'domain': 'moviesapp.dev',
            'name': 'moviesapp.dev'
        }
    )


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(update_site_forward, update_site_backward),
    ]
