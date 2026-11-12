import re

from django import forms
from django.utils import timezone

from .models import Enquiry


class BaseEnquiryForm(forms.ModelForm):
    # Trap for spam bots. People never see this field (it is hidden with CSS),
    # so anything typed into it means the form was filled in by a script.
    leave_blank = forms.CharField(
        required=False,
        label="Leave this field empty",
        widget=forms.TextInput(attrs={'tabindex': '-1', 'autocomplete': 'off'}),
    )

    def clean_leave_blank(self):
        if self.cleaned_data.get('leave_blank'):
            raise forms.ValidationError("Spam detected.")
        return ''

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()
        if not re.fullmatch(r'\+?[\d\s-]{9,18}', phone):
            raise forms.ValidationError(
                "Enter a phone number we can call, like +254 712 345 678."
            )
        return phone


class BookingForm(BaseEnquiryForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'phone', 'email', 'pet_name', 'preferred_date', 'message']
        labels = {
            'name': 'Your name',
            'phone': 'Phone number',
            'email': 'Email (optional)',
            'pet_name': "Pet's name",
            'preferred_date': 'Preferred date',
            'message': 'What is the visit for?',
        }
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'name'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'autocomplete': 'tel', 'placeholder': '+254 712 345 678'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'email'}),
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pet_name'].required = True
        self.fields['preferred_date'].required = True
        self.fields['message'].required = True

    def clean_preferred_date(self):
        date = self.cleaned_data.get('preferred_date')
        if date and date < timezone.localdate():
            raise forms.ValidationError("Choose today or a later date.")
        return date


class ContactForm(BaseEnquiryForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'phone', 'email', 'message']
        labels = {
            'name': 'Your name',
            'phone': 'Phone number',
            'email': 'Email (optional)',
            'message': 'Your message',
        }
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'name'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'autocomplete': 'tel', 'placeholder': '+254 712 345 678'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'email'}),
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].required = True
