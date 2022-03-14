# Generated by Django 4.0.2 on 2022-03-14 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qnaboard', '0003_alter_answer_author_alter_answer_like_users_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('has_answer', models.BooleanField(default=True)),
            ],
        ),
    ]
