# Generated by Django 2.0.8 on 2019-12-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20191229_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='title',
            field=models.CharField(default='默认', max_length=50, verbose_name='试卷名'),
        ),
    ]
