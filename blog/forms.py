from django import forms

from .models import Post
from .widgets import XDSoftDateTimePickerInput, BootstrapMarkdownInput


class PostForm(forms.ModelForm):
    published_at = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=XDSoftDateTimePickerInput(format='%d/%m/%Y %H:%M'),
    )

    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'meta_title',
            'desc',
            'banner',
            'thumb',
            'content',
            'meta_tags',
            'order',
            'published_at'
        ]
        widgets = {
            'desc': forms.Textarea(attrs={'rows': 2}),
            'meta_tags': forms.Textarea(attrs={'rows': 1}),
            'content': BootstrapMarkdownInput(),
        }
