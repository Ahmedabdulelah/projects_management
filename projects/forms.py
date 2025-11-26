from django import forms
from . import models
from django.utils.translation import gettext as _

attrs = {'class': 'form-control'}

class ProjectCreateFrom(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        labels = {
            'category': _('Category'),
            'title': _('Title'),
            'description': _('Description')
        }
        widgets ={
            'category': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs)
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = _("اختر التصنيف")




class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields= ['category', 'title', 'status']
        widgets= {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'status': forms.Select(attrs=attrs)
        }