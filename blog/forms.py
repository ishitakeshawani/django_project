from django import forms
from .models import *

class student_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your name'}), required=True, max_length=50)
    enno = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'enter your enrollment no'}), required=True)
    sem = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'enter your semester'}), required=True)
    branch = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your branch'}), required=True, max_length=8)
    subject1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your submane'}), required=True,max_length=15)
    subject2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your subname'}),max_length=15)
    subject3 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your subname'}),max_length=15)
    subject4 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your subname'}),max_length=15)
    subject5 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your subname'}),max_length=15)
    outofmid1 = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter totalmarks of sub1'}),required=True)
    outofmid2 = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter totalmarks of sub2'}),required=True)
    outofmid3 = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter totalmarks of sub3'}),required=True)
    outofmid4 = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter totalmarks of sub4'}),required=True)
    outofmid5 = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter totalmarks of sub5'}),required=True)
    sub1mark = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your sub1mark'}),required=True)
    sub2mark = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your sub2mark'}),required=True)
    sub3mark = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your sub3mark'}),required=True)
    sub4mark = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your sub4mark'}),required=True)
    sub5mark = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your sub5mark'}),required=True)
    remidsub1mark = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your remidmark of subject'}),required=True)
    remidsub2mark = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your remidmark of subject'}),required=True)
    remidsub3mark = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your remidmark of subject'}),required=True)
    remidsub4mark = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your remidmark of subject'}),required=True)
    remidsub5mark = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your remidmark of subject'}),required=True)

    class Meta():
        model = Enroll
        fields = ['name','enno', 'sem','branch','subject1','subject2','subject3','subject4',
                  'subject5','sub1mark','sub2mark','sub3mark','sub4mark','sub5mark',
                  'outofmid1','outofmid2','outofmid3','outofmid4','outofmid5',
                  'remidsub1mark','remidsub2mark','remidsub3mark','remidsub4mark','remidsub5mark'

                  ]
