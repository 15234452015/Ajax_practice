from django import forms
from stu.models import Student,Clazz

class ClazzForm(forms.ModelForm):
    class Meta:
        Model = Clazz
        fields = ('cname',)


class StudentForm(forms.ModelForm):
    class Meta:
        Model = Student
        fields = ('sname',)