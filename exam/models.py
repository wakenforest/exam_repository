from django.db import models

# Create your models here.

# 为性别,部门 指定备选字段
SEX=(
    ('男','男'),
    ('女','女'),
)

DEPT=(
    ('总体室','总体室'),
    ('软件室','软件室'),
    ('设备室','设备室'),
    ('管控室','管控室'),
    ('保障室','保障室'),
)

ANSWER=(
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
)

ANSWER_M=(
    ('A','A'),
    ('A,B','A,B'),
    ('A,C','A,C'),
    ('A,D','A,D'),
    ('A,B,C','A,B,C'),
    ('A,B,D','A,B,D'),
    ('A,C,D','A,C,D'),
    ('A,B,C,D','A,B,C,D'),
    ('B','B'),
    ('B,C','B,C'),
    ('B,D','B,D'),
    ('B,C,D','B,C,D'),
    ('C','C'),
    ('C,D','C,D'),
    ('D','D'),
)

class Student(models.Model):
    id=models.CharField('编号',max_length=20,primary_key=True)
    name=models.CharField('姓名',max_length=20)
    sex=models.CharField('性别',max_length=4,choices=SEX,default='男')
    dept=models.CharField('部门',max_length=20,choices=DEPT,default=None)
    password=models.CharField('密码',max_length=20,default='111111')

    class Meta:
        #db_table='student'
        verbose_name='受训人'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id

class Officer(models.Model):
    id=models.CharField('编号',max_length=20,primary_key=True)
    name=models.CharField('姓名',max_length=20)
    sex=models.CharField('性别',max_length=4,choices=SEX,default='男')
    dept=models.CharField('部门',max_length=20,choices=DEPT,default=None)
    password=models.CharField('密码',max_length=20,default='123456')

    class Meta:
        #db_table='officer'
        verbose_name='施训人'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id

class Subject(models.Model):
    id=models.CharField('科目编号',max_length=20,primary_key=True)
    title=models.CharField('科目名',max_length=50)

    class Meta:
        #db_table='subject'
        verbose_name='科目'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title


class SingleChoiceQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    title = models.TextField('题目')
    optionA=models.CharField('A选项',max_length=255)
    optionB=models.CharField('B选项',max_length=255)
    optionC=models.CharField('C选项',max_length=255)
    optionD=models.CharField('D选项',max_length=255)
    answer=models.CharField('答案',max_length=10,choices=ANSWER)
    score=models.IntegerField('分数',default=1)

    class Meta:
        #db_table='single_choice_question'
        verbose_name='单项选择题库'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '<%s:%s>'%(self.subject,self.title)

class MultiChoiceQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    title = models.TextField('题目')
    optionA=models.CharField('A选项',max_length=255)
    optionB=models.CharField('B选项',max_length=255)
    optionC=models.CharField('C选项',max_length=255)
    optionD=models.CharField('D选项',max_length=255)
    answer=models.CharField('答案',max_length=10,choices=ANSWER_M)
    score=models.IntegerField('分数',default=2)

    class Meta:
        #db_table='multi_choice_question'
        verbose_name='多项选择题库'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '<%s:%s>'%(self.subject,self.title)

class Paper(models.Model):
    #题号id 和题库为多对多的关系
    id = models.AutoField(primary_key=True)
    title = models.CharField('试卷名',max_length=50,default='默认')
    #title = '试卷名'
    sid=models.ManyToManyField(SingleChoiceQuestion)#多对多
    mid=models.ManyToManyField(MultiChoiceQuestion)#多对多
    tid=models.ForeignKey(Officer,on_delete=models.CASCADE)#添加外键
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    examperiod = models.IntegerField('考试时长',default=45)
    examtime=models.DateTimeField()

    class Meta:
        #db_table='paper'
        verbose_name='试卷'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title



class Grade(models.Model):
    sid=models.ForeignKey(Student,on_delete=models.CASCADE,default='')#添加外键
    paper_title=models.CharField('试卷名',max_length=50,default='默认')
    # subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    # subject=models.CharField('科目',max_length=20,default='')
    grade=models.IntegerField()

    def __str__(self):
        return '<%s:%s>'%(self.sid,self.grade)

    class Meta:
        db_table='grade'
        verbose_name='成绩'
        verbose_name_plural=verbose_name