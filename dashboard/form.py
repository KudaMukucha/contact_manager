from django import forms
from .models import Contact

class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('user','is_deleted','created_at','updated_at')

        