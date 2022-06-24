# Generated by Django 4.0.5 on 2022-06-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='version',
            new_name='version_mke',
        ),
        migrations.AddField(
            model_name='snippet',
            name='version_release',
            field=models.TextField(default='1.0.1'),
            preserve_default=False,
        ),
    ]