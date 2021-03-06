# Generated by Django 2.0.8 on 2020-01-04 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_delete_paperrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('paper_title', models.CharField(default='测试', max_length=50, verbose_name='试卷名')),
                ('stu_id', models.CharField(max_length=20, verbose_name='学生编号')),
                ('answerList', models.CharField(default='', max_length=255, verbose_name='答案记录')),
            ],
            options={
                'verbose_name': '试卷记录',
                'verbose_name_plural': '试卷记录',
            },
        ),
    ]
