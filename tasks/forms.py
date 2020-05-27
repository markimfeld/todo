from django import forms

from tasks.models import (
    ListTask, 
    Task, 
    Tag
)

class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('completed',)
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Check email, do something, etc..',
                }
            )
        }

class NewListForm(forms.ModelForm):
    class Meta:
        model = ListTask
        fields = '__all__'
        exclude = ('last_edited_date',)
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Title...'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs = {
                    'class': 'form-control'
                }
            )
        }

class NewTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Tag name...'
                }
            )
        }