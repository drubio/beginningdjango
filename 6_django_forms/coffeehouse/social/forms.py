from django import forms


class SharingForm(forms.Form):
    # NOTE: forms.PhotoField requires Python PIL & other operating system libraries,
    #       so generic FileField is used instead
    video = forms.FileField()
    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
