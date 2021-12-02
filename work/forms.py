from django import forms

from .models import Country
from .models import Diseasetype
from .models import Disease
from .models import Discover
from .models import Users
from .models import Publicservant
from .models import Doctor
from .models import Specialize
from .models import Record

class C(forms.ModelForm):

    class Meta:
        model = Country
        fields = ('cname', 'population',)
class DT(forms.ModelForm):

    class Meta:
        model = Diseasetype
        fields = ('id', 'description')
class Dise(forms.ModelForm):

    class Meta:
        model = Disease
        fields = ('id', 'disease_code','pathogen', 'description')
class Disc(forms.ModelForm):

    class Meta:
        model = Discover
        fields = ('cname', 'disease_code', 'first_enc_date',)
class U(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('email', 'name', 'surname', 'salary', 'phone', 'cname',)

class P(forms.ModelForm):

    class Meta:
        model = Publicservant
        fields = ('email', 'department',)

class Doc(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ('email', 'degree',)

class S(forms.ModelForm):

    class Meta:
        model = Specialize
        fields = ('id', 'email',)

class R(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('email', 'cname', 'disease_code', 'total_deaths', 'total_patients')
