# Generated by Django 4.0.2 on 2022-03-10 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_recruit_personnel'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='select',
            field=models.CharField(choices=[('2022년 강서구 빅데이터 활용 공모전', '강서구'), ('2022년 노원구 빅데이터 활용 공모전', '노원구')], max_length=80, null=True),
        ),
    ]
