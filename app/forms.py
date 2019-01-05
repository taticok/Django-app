from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name','start_date','end_date','memo')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':''}),
                    'start_date': forms.TextInput(attrs={'placeholder':'2019-01-01'}),
                    'end_date': forms.TextInput(attrs={'placeholder':'2019-01-01'}),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }