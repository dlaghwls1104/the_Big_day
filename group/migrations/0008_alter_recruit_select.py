# Generated by Django 4.0.2 on 2022-03-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0007_merge_0003_recruit_select_0006_alter_recruit_select'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='select',
            field=models.CharField(choices=[('2022년 강서구 빅데이터 활용 공모전', '2022년 강서구 빅데이터 활용 공모전'), ('2022년 빅데이터캠퍼스 멘토링 멘티 모집', '2022년 빅데이터캠퍼스 멘토링 멘티 모집')], max_length=80, null=True),
        ),
    ]
