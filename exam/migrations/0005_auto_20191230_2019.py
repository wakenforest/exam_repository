# Generated by Django 2.0.8 on 2019-12-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='subject',
        ),
        migrations.AddField(
            model_name='grade',
            name='paper_title',
            field=models.CharField(default='默认', max_length=50, verbose_name='试卷名'),
        ),
    ]
