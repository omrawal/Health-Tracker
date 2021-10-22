from django import forms
from .models import Statistic


class StatisticCreate(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ('weight', 'height', 'age', 'gender', 'user')
        # fields = '__all__'
