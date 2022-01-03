from django import forms
from .models import Post, Comment


class PostCreateModelForm(forms.ModelForm):
    title = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Enter Post details','class': 'create_post_input','type': 'text','style': 'width: 100%;'}))
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Enter your post title','name':'comment[text]','id':'comment[text]','cols':'60','class':'ui-autocomplete-input','autocomplete':'off','role':'textbox','aria-autocomplete':'list','aria-haspopup':'true','style':'margin-top: 10px; margin-bottom: 0px; height: 200px;'}))
    class Meta:
        model = Post
        fields = ('title','content')

class PostModelForm(forms.ModelForm):
    content = forms.Textarea(attrs={'name':'comment[text]','id':'comment[text]','cols':'60','class':'ui-autocomplete-input','autocomplete':'off','role':'textbox','aria-autocomplete':'list','aria-haspopup':'true','style':'margin-top: 10px; margin-bottom: 0px; height: 300px;'})
    class Meta:
        model = Post
        fields = ('content',)

class CommentModelForm(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder' : 'Comment here...','name':'comment[text]','id':'comment[text]','cols':'60','class':'ui-autocomplete-input','autocomplete':'off','role':'textbox','aria-autocomplete':'list','aria-haspopup':'true','style':'margin-top: 10px; margin-bottom: 0px; height: 50px;'}))
    class Meta:
        model = Comment
        fields = ('body',)