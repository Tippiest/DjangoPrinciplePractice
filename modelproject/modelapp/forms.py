from django.forms import ModelForm


#import Logger model from models file
from .models import Logger

class LogForm(ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'

