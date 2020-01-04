from django.shortcuts import render,redirect,reverse
from exam import models
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth import logout
import operator
import os
from django.conf import settings
import xlrd

# Create your views here.
def index(request):
    return render(request,'index.html')

def toIndex(request):
    return render(request,'index.html')

# 学生登陆 视图函数
def studentLogin(request):
    if request.method=='POST':
        # 获取表单信息
        stuId=request.POST.get('id')
        password=request.POST.get('password')
        print("id",stuId,"password",password)
        # 通过学号获取该学生实体
        try:
            student=models.Student.objects.get(id=stuId)
            print(student)
        except:
            return render(request,'index.html',{'message':'无受训人信息'})

        if password==student.password:  #登录成功
            #查询考试信息
            paper=models.Paper.objects.filter()
            grade=models.Grade.objects.filter(sid=stuId)
            return render(request,'index.html',{'student':student,'paper':paper,'grade':grade})
            #查询成绩信息
            # grade=models.Grade.objects.filter(sid=student.id)
            # 渲染index模板
            # return render(request,'index.html',{'student':student,'paper':paper,'grade':grade})

        else:return render(request,'index.html',{'message':'密码不正确'})

# 教师登陆 视图函数
def OfficerLogin(request):

    if request.method == 'POST':
        teaId = request.POST.get('id')
        password = request.POST.get('password')
        # print("id", teaId, "password", password)

        teacher = models.Officer.objects.get(id=teaId)
        print(teacher)
        if password == teacher.password:  # 登录成功
            # 实现成绩统计功能
            #在试卷表 paper 找到该老师发布的试题
            paper=models.Paper.objects.filter(tid=teacher.id)

            data1=models.Grade.objects.filter(paper_title='管理控制1',grade__lt=60).count()
            data2=models.Grade.objects.filter(paper_title='管理控制1',grade__gte=60,grade__lt=70).count()
            data3 = models.Grade.objects.filter(paper_title='管理控制1', grade__gte=70, grade__lt=80).count()
            data4 = models.Grade.objects.filter(paper_title='管理控制1', grade__gte=80, grade__lt=90).count()
            data5 = models.Grade.objects.filter(paper_title='管理控制1', grade__gte=90).count()

            # data6 = models.Grade.objects.filter(paper_title='数据库原理', grade__lt=60).count()
            # data7= models.Grade.objects.filter(paper_title='数据库原理', grade__gte=60, grade__lt=70).count()
            # data8= models.Grade.objects.filter(paper_title='数据库原理', grade__gte=70, grade__lt=80).count()
            # data9 = models.Grade.objects.filter(paper_title='数据库原理', grade__gte=80, grade__lt=90).count()
            # data10= models.Grade.objects.filter(paper_title='数据库原理', grade__gte=90).count()

            data_1={'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5}
            # data_2 = {'data6': data6, 'data7': data7, 'data8': data8, 'data9': data9, 'data10': data10}

            print("数量：",data2)
            return render(request, 'teacher.html', {'teacher': teacher, 'paper':paper,'data_1':data_1})

        else:
            return render(request, 'index.html', {'message': '密码不正确'})

#学生考试 的视图函数
def startExam(request):
    sid = request.GET.get('sid')
    subject1=request.GET.get('subject')
    paper_id = request.GET.get('paperid')

    student=models.Student.objects.get(id=sid)
    # paper=models.Paper.objects.filter(subject=subject1)
    paper=models.Paper.objects.filter(id=paper_id)
    print(paper)
    # print('学号',sid,'考试科目',subject1)
    return render(request,'exam.html',{'student':student,'paper':paper,'subject':subject1})


#计算由exam.html模版传过来的数据计算成绩
def calGrade(request):

    if request.method=='POST':
        # 得到学号和科目
        sid=request.POST.get('sid')
        paper_id = request.POST.get('paper_id')
        subject1 = request.POST.get('subject')

        # 重新生成Student实例，Paper实例，Grade实例，名字和index中for的一致，可重复渲染
        student= models.Student.objects.get(id=sid)
        paper = models.Paper.objects.filter(id=paper_id)
        # paper = models.Paper.objects.filter()
        grade = models.Grade.objects.filter(sid=student.id)

        # 计算该门考试的学生成绩
        question_single= models.Paper.objects.filter(id=paper_id).values("sid").values('sid__id','sid__title','sid__answer','sid__score')
        question_multi = models.Paper.objects.filter(id=paper_id).values("mid").values('mid__id','mid__title','mid__answer','mid__score')

        mygrade=0#初始化一个成绩为0
        fullgrade=0
        for p in question_single:
            qId=str(p['sid__title'])#int 转 string,通过sid找到题号
            myans=request.POST.get(qId)#通过 qid 得到学生关于该题的作答
            okans=p['sid__answer']#得到正确答案
            # print(okans)
            if myans==okans:#判断学生作答与正确答案是否一致
                mygrade+=p['sid__score']#若一致,得到该题的分数,累加mygrade变量
            fullgrade+=p['sid__score']
        
        for p in question_multi:
            qId=str(p['mid__title'])#int 转 string,通过sid找到题号
            myans=request.POST.getlist(qId)#通过 qid 得到学生关于该题的作答
            okans=p['mid__answer']#得到正确答案
            okans = okans.split(',')
            if operator.eq(myans,okans):#判断学生作答与正确答案是否一致
                mygrade+=p['mid__score']#若一致,得到该题的分数,累加mygrade变量
            fullgrade+=p['mid__score']

        mygrade = mygrade/fullgrade * 100
        #向Grade表中插入数据
        paper_inst = paper.get(id=paper_id)
        for grade_inst in grade:
            if (grade_inst.sid.id)==(sid) and grade_inst.paper_title==paper_inst.title:
                grade = models.Grade.objects.filter(sid=student.id)
                paper = models.Paper.objects.all()
                return render(request,'index.html',{'student':student,'paper':paper,'grade':grade,'message':'考试已完成'})


        models.Grade.objects.create(sid_id=sid,paper_title=paper_inst.title,grade=mygrade)
        grade = models.Grade.objects.filter(sid=student.id)
        paper = models.Paper.objects.all()
        # print(mygrade)
        # 重新渲染index.html模板
        # return redirect(reverse())
        # return HttpResponseRedirect('/')
        return render(request,'index.html',{'student':student,'paper':paper,'grade':grade})
        

# 教师退出
def logOut(request):
    return redirect('/')
    # return redirect('/toIndex/')

def upSingleChoice(request):
    
    teaId=request.POST.get('tid')

    # singleCholiceUpload
    uploadedFile = request.FILES.get('singleCholiceUpload')
    
    filePath = os.path.join(settings.UPLOAD_ROOT,uploadedFile.name)
    print(filePath)

    book = xlrd.open_workbook(filePath)

    sheet = book.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    print(rows)
    print(cols)

    for i in range(1,rows):   # sheet.cell_value(i,1) 选项A
        title = sheet.cell_value(i,0)
        opA = sheet.cell_value(i,1)
        opB = sheet.cell_value(i,2)
        opC = sheet.cell_value(i,3)
        opD = sheet.cell_value(i,4)
        answer = sheet.cell_value(i,5)
        subjectTitle = sheet.cell_value(i,6)
        isSingle = sheet.cell_value(i,7)

        if isSingle=="单选":
            subject_tmp = models.Subject.objects.get(title=subjectTitle)
            scQuestionList = models.SingleChoiceQuestion.objects.all()
            
            validated_data = dict()
            print(subject_tmp)
            validated_data['id'] = subject_tmp.id
            validated_data['title'] = subjectTitle
            subject_ins = models.Subject(**validated_data)

            flag_ques = 0

            for scQuestion in scQuestionList:
                if scQuestion.title==title:
                    flag_ques = 1
                    break

            if flag_ques==0:
                models.SingleChoiceQuestion.objects.create(subject=subject_ins,title=title,optionA=opA,optionB=opB,
                optionC=opC,optionD=opD,answer=answer,score=1)

    teacher=models.Officer.objects.get(id=teaId)
    paper=models.Paper.objects.filter(tid=teacher.id)
    data_1 = {}

    return render(request, 'teacher.html', {'teacher': teacher, 'paper':paper,'data_1':data_1})



def upMultiChoice(request):
    
    teaId=request.POST.get('tid')

    # multiCholiceUpload
    uploadedFile = request.FILES.get('multiCholiceUpload')
    
    filePath = os.path.join(settings.UPLOAD_ROOT,uploadedFile.name)
    print(filePath)

    book = xlrd.open_workbook(filePath)

    sheet = book.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    print(rows)
    print(cols)

    for i in range(1,rows):   # sheet.cell_value(i,1) 选项A
        title = sheet.cell_value(i,0)
        opA = sheet.cell_value(i,1)
        opB = sheet.cell_value(i,2)
        opC = sheet.cell_value(i,3)
        opD = sheet.cell_value(i,4)
        answer = sheet.cell_value(i,5)
        subjectTitle = sheet.cell_value(i,6)
        isMulti = sheet.cell_value(i,7)

        if isMulti=="多选":
            subject_tmp = models.Subject.objects.get(title=subjectTitle)
            scQuestionList = models.MultiChoiceQuestion.objects.all()
            
            validated_data = dict()
            print(subject_tmp)
            validated_data['id'] = subject_tmp.id
            validated_data['title'] = subjectTitle
            subject_ins = models.Subject(**validated_data)

            print( (subject_ins.id) )

            flag_ques = 0

            for scQuestion in scQuestionList:
                if scQuestion.title==title:
                    flag_ques = 1
                    break

            if flag_ques==0:
                models.MultiChoiceQuestion.objects.create(subject=subject_ins,title=title,optionA=opA,optionB=opB,
                optionC=opC,optionD=opD,answer=answer,score=2)

    teacher=models.Officer.objects.get(id=teaId)
    paper=models.Paper.objects.filter(tid=teacher.id)
    data_1 = {}
    
    return render(request, 'teacher.html', {'teacher': teacher, 'paper':paper,'data_1':data_1})