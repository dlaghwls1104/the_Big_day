# Generated by Django 4.0.2 on 2022-03-13 07:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0008_alter_challenge_date_finish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='date_finish',
            field=models.DateField(default=datetime.datetime(2022, 3, 20, 7, 27, 18, 572457, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2022, 3, 13, 7, 27, 18, 572350, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenge', to=settings.AUTH_USER_MODEL),
        ),
    ]
