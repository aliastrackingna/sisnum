from django import forms
from .models import TipoDocumento


class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Memorando, Ofício, Circular...',
                'required': True
            })
        }
