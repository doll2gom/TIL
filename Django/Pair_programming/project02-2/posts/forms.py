from django import forms
from .models import Post
choices_category = (
    ('','category'),
    ('개발','개발'),
    ('CS','CS'),
    ('신기술','신기술'),
)

class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Post
        fields = ('title','content','category', 'image')

    

    category = forms.CharField(
        widget= forms.Select(
            choices = choices_category
            # attrs={
            #      'aria-label':"Default select example",
            # }
        )
        # widget = {
        #     'category':forms.Select(attrs={'class':'form-category'})
        # }
    )



