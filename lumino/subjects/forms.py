from django import forms
from django.forms import modelformset_factory
from .models import  Subject, Enrollment
from .widgets import MarkInput


class SubjectEnrollForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=None,
    )

    def __init__(self,user_pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subjects'].queryset = Subject.objects.exclude(enrollments__student__pk = user_pk)
    def save(self, user):
        for subject in self.cleaned_data['subjects']:
            subject.enroll(user)

class SubjectUnenrollForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=None,
    )
    def __init__(self,user_pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subjects'].queryset = Subject.objects.filter(enrollments__student__pk = user_pk)

    def save(self, user):
        for subject in self.cleaned_data['subjects']:
            subject.unenroll(user)

class EnrollmentMarkForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["mark"]
        widgets ={
            "mark":MarkInput()
        }

EnrollmentMarkFormSet = modelformset_factory(
    Enrollment,
    form=EnrollmentMarkForm,
    extra=0 
)