from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


# Inner class 개념? 파이썬 문법과 아무런 상관없다.
# 그냥 django ModelForm의 구조가 이렇게 설계되었을 뿐
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력해주세요.'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={'class': 'my-content'},
        ),
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

    # ModelForm의 정보를 작성하는 곳
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('content',)
        # exclude = ('title',)
