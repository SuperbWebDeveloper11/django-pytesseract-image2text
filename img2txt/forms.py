from django import forms 


class ImageForm(forms.Form):
    LANGUAGES = (
        ('eng', 'English'),
        ('fra', 'French'),
    )
    image = forms.ImageField()
    language = forms.ChoiceField(choices=LANGUAGES)


