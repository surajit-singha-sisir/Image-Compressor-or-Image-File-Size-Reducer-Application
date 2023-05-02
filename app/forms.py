from django import forms

class ImageForm(forms.Form):
    image = forms.ImageField()
    compression_percentage = forms.IntegerField(initial=60, min_value=10, max_value=100, label='Compression Percentage')
