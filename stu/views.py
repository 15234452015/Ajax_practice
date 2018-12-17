from django.http import HttpResponse
from django.shortcuts import render
from django import forms
# Create your views here.
from django.views import View

from stu.forms import ClazzForm, StudentForm


class Register(View):
    def get(self,request):
        clsFrm = ClazzForm()
        stuFrm = StudentForm()
        return render(request,'register.html',{'clsFrm':clsFrm,'stuFrm':stuFrm})


    def post(self,request):
        clsFrm = ClazzForm(request.POST)
        stuFrm = StudentForm(request.POST)
        if clsFrm.is_valid() and stuFrm.is_valid():
            newcls = clsFrm.save()
            newstu = stuFrm.save(commit=False)
            newstu.clazz = newcls
            newstu.save()
            return HttpResponse(u'注册成功')
        return HttpResponse(u'注册失败')