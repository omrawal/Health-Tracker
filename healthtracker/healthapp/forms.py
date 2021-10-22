from django import forms
from .models import Statistic


class StatisticCreate(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = '__all__'
