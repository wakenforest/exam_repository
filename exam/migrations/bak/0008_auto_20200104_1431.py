# Generated by Django 2.0.8 on 2020-01-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_paperrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperrecord',
            name='stu_id',
            field=models.CharField(max_length=20, primary_key=True, verbose_name='学生编号'),
        ),
    ]
