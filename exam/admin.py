from django.contrib import admin
from .models import Student,Officer,Paper,Subject,SingleChoiceQuestion,MultiChoiceQuestion,Grade

# Register your models here.

admin.site.site_header='在线考试系统后台'
admin.site.site_title='在线考试系统'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','dept','password')# 要显示哪些信息
    list_display_links = ('id','name')#点击哪些信息可以进入编辑页面
    search_fields = ['name','dept']   #指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter =['name','dept']#指定列表过滤器，右边将会出现一个快捷的过滤选项

@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','dept','password')# 要显示哪些信息
    list_display_links = ('id','name')#点击哪些信息可以进入编辑页面
    search_fields = ['name','dept']   #指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter =['name','dept']#指定列表过滤器，右边将会出现一个快捷的过滤选项

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id','title')# 要显示哪些信息
    list_display_links = ('id','title')#点击哪些信息可以进入编辑页面
    search_fields = ['title']   #指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter =['title']#指定列表过滤器，右边将会出现一个快捷的过滤选项

@admin.register(SingleChoiceQuestion)
class SingleChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ('id','subject','title','optionA','optionB','optionC','optionD','answer','score')

@admin.register(MultiChoiceQuestion)
class MultiChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ('id','subject','title','optionA','optionB','optionC','optionD','answer','score')

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('tid','title','subject','examtime')
    list_display_links = ('tid','title','subject','examtime')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('sid','paper_title','grade')
    list_display_links = ('sid','paper_title','grade')