# Generated by Django 4.1.2 on 2022-12-15 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_artikel_options_alter_artikel_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
