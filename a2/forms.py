from django.forms import ModelForm
from stu.models import Stu

class StudentForm(ModelForm):
    class Meta:
        model = Stu
        fields = "__all__"