from django import forms
from status.models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    # This validation is like tweet which tells us that our length of content must be <=248
    def clean_content(self ,*args , **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 248:
            raise forms.ValidationError("Content is too long!")
        return content

    def clean(self , *args , **kwargs):
        data = self.cleaned_data
        content = data.get('content',None)
        if content == "":
            content = None
        image = data.get("image",None)
        if content is None and image is None:
            raise forms.ValidationError("At least one of image or content is required!")
        return super().clean(*args,**kwargs)
