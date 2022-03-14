# Generated by Django 4.0.2 on 2022-03-14 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qnaboard', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_question', to='qnaboard.category'),
            preserve_default=False,
        ),
    ]
