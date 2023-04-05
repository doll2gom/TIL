from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder':'제목을 입력해주세요.'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder':'내용을 입력해주세요.'
            },
        ),
    ),
    completed = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'type': 'radio'}
        )
    )
    
    priority = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'min': 1, 'max': 5, 'value': 3},
        )
    )
    deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'},
        ),
    )    
    
    class Meta:
        model = Todo
        fields = '__all__'