# Generated by Django 3.1.5 on 2021-01-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_site_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
