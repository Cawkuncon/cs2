# Generated by Django 4.0.6 on 2022-08-11 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csinf', '0006_alter_notice_options_notice_count_skins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='count_skins',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
