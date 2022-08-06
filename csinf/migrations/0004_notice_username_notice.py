# Generated by Django 4.0.6 on 2022-08-06 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('csinf', '0003_alter_notice_skin_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='username_notice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
