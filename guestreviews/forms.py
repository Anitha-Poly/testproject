from django import forms

from guestreviews.models import admini, library, guest, public, Book


class adminiForm(forms.ModelForm):
    class Meta:
        model=admini
        fields= "__all__"
class guestForm(forms.ModelForm):
    class Meta:
        model=guest
        fields= "__all__"

class publicForm(forms.ModelForm):
    class Meta:
        model=public
        fields= "__all__"

class libraryForm(forms.ModelForm):
    class Meta:
        model=library
        fields= "__all__"
class bookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields= "__all__"