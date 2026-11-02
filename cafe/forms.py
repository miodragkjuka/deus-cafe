import datetime

from django import forms

from .models import ContactMessage, Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'date', 'time', 'guests', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError('Датумот не може да биде во минатото.')
        return date

    def clean_guests(self):
        guests = self.cleaned_data['guests']
        if not 1 <= guests <= 20:
            raise forms.ValidationError('Внесете број на гости од 1 до 20.')
        return guests


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {'message': forms.Textarea(attrs={'rows': 5})}
