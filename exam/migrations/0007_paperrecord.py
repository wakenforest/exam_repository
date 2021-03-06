# Generated by Django 2.0.8 on 2020-01-04 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_paper_examperiod'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stu_id', models.CharField(max_length=20, verbose_name='学生编号')),
                ('answerList', models.CharField(default='', max_length=255, verbose_name='答案记录')),
                ('paperid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Paper')),
            ],
            options={
                'verbose_name': '试卷记录',
                'verbose_name_plural': '试卷记录',
            },
        ),
    ]
