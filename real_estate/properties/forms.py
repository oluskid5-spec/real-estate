from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your email address", "class": "form-control"}),
            "phone": forms.TextInput(attrs={"placeholder": "Your phone number", "class": "form-control"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell us what you are looking for...", "class": "form-control", "rows": 5}),
        }
