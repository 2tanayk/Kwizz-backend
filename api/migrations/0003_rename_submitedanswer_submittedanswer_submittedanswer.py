# Generated by Django 4.0.2 on 2022-02-17 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_submittedanswer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submittedanswer',
            old_name='submitedAnswer',
            new_name='submittedAnswer',
        ),
    ]
