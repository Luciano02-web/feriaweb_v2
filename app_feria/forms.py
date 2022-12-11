from distutils.command.upload import upload
from tkinter import CASCADE
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import User

from app_feria.models import *
"""
from app_feria.models import Avatar, Imagen"""

"""

OPCIONESGENERO=[
    ('Hombre','Hombre'),('Mujer','Mujer')
]
genero = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPCIONESGENERO)
genero = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[('Hombre','Hombre'),('Mujer','Mujer')])
"""

"""
class FormuJean(forms.Form):
    imagen = forms.ImageField(required=False)
    imagen_b = forms.ImageField(required=False)
    codigo = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Codigo(Requerido, Unico)'}))
    talle = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'placeholder':'Talle'}))
    color = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'placeholder':'Color'}))
    precio = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Precio(Requerido)'}))
    class Meta:
        model = Imagen
        fields = ["imagen","imagen_b"]
        model = Jean
        fields = ["genero"]
"""
class FormuJean(forms.ModelForm):
    class Meta:
        model = Jean
        fields = ["imagen","imagen_b","codigo","talle","color","precio","genero",]
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder':'Codigo(Requerido, Unico)'}),
            'talle': forms.TextInput(attrs={'placeholder':'Talle'}),
            'color': forms.TextInput(attrs={'placeholder':'Color'}),
            'precio': forms.TextInput(attrs={'placeholder':'Precio(Requerido)'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen_b'].widget.attrs.update({'class':'form-control'})
        self.fields['codigo'].widget.attrs.update({'class':'form-control'})
        self.fields['talle'].widget.attrs.update({'class':'form-control'})
        self.fields['color'].widget.attrs.update({'class':'form-control'})
        self.fields['precio'].widget.attrs.update({'class':'form-control'})
        self.fields['genero'].widget.attrs.update({'class':'form-control'})
"""
 widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'instrumento' : forms.Select(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoContacto' : forms.TextInput(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }
"""
class FormuRemera(forms.ModelForm):
    class Meta:
        model = Remera
        fields = ["imagen","imagen_b","codigo","talle","color","precio","genero",]
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder':'Codigo(Requerido, Unico)'}),
            'talle': forms.TextInput(attrs={'placeholder':'Talle'}),
            'color': forms.TextInput(attrs={'placeholder':'Color'}),
            'precio': forms.TextInput(attrs={'placeholder':'Precio(Requerido)'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen_b'].widget.attrs.update({'class':'form-control'})
        self.fields['codigo'].widget.attrs.update({'class':'form-control'})
        self.fields['talle'].widget.attrs.update({'class':'form-control'})
        self.fields['color'].widget.attrs.update({'class':'form-control'})
        self.fields['precio'].widget.attrs.update({'class':'form-control'})
        self.fields['genero'].widget.attrs.update({'class':'form-control'})


class FormuCamisa(forms.ModelForm):
    class Meta:
        model = Camisa
        fields = ["imagen","imagen_b","codigo","talle","color","precio","genero",]
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder':'Codigo(Requerido, Unico)'}),
            'talle': forms.TextInput(attrs={'placeholder':'Talle'}),
            'color': forms.TextInput(attrs={'placeholder':'Color'}),
            'precio': forms.TextInput(attrs={'placeholder':'Precio(Requerido)'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen_b'].widget.attrs.update({'class':'form-control'})
        self.fields['codigo'].widget.attrs.update({'class':'form-control'})
        self.fields['talle'].widget.attrs.update({'class':'form-control'})
        self.fields['color'].widget.attrs.update({'class':'form-control'})
        self.fields['precio'].widget.attrs.update({'class':'form-control'})
        self.fields['genero'].widget.attrs.update({'class':'form-control'})

class FormuCampera(forms.ModelForm):
    class Meta:
        model = Campera
        fields = ["imagen","imagen_b","codigo","talle","color","precio","genero",]
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder':'Codigo(Requerido, Unico)'}),
            'talle': forms.TextInput(attrs={'placeholder':'Talle'}),
            'color': forms.TextInput(attrs={'placeholder':'Color'}),
            'precio': forms.TextInput(attrs={'placeholder':'Precio(Requerido)'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen_b'].widget.attrs.update({'class':'form-control'})
        self.fields['codigo'].widget.attrs.update({'class':'form-control'})
        self.fields['talle'].widget.attrs.update({'class':'form-control'})
        self.fields['color'].widget.attrs.update({'class':'form-control'})
        self.fields['precio'].widget.attrs.update({'class':'form-control'})
        self.fields['genero'].widget.attrs.update({'class':'form-control'})
    

class FormuTodo100(forms.ModelForm):
    class Meta:
        model = Todo100
        fields = ["imagen","imagen_b","codigo","talle","color","precio","genero",]
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder':'Codigo(Requerido, Unico)'}),
            'talle': forms.TextInput(attrs={'placeholder':'Talle'}),
            'color': forms.TextInput(attrs={'placeholder':'Color'}),
            'precio': forms.TextInput(attrs={'placeholder':'Precio(Requerido)'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen_b'].widget.attrs.update({'class':'form-control'})
        self.fields['codigo'].widget.attrs.update({'class':'form-control'})
        self.fields['talle'].widget.attrs.update({'class':'form-control'})
        self.fields['color'].widget.attrs.update({'class':'form-control'})
        self.fields['precio'].widget.attrs.update({'class':'form-control'})
        self.fields['genero'].widget.attrs.update({'class':'form-control'})

class FormuCalzado(forms.ModelForm):
    class Meta:
        model = Calzado
        fields = ["imagen","imagen_b","codigo","talle","color","precio","genero",]
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder':'Codigo(Requerido, Unico)'}),
            'talle': forms.TextInput(attrs={'placeholder':'Talle'}),
            'color': forms.TextInput(attrs={'placeholder':'Color'}),
            'precio': forms.TextInput(attrs={'placeholder':'Precio(Requerido)'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen_b'].widget.attrs.update({'class':'form-control'})
        self.fields['codigo'].widget.attrs.update({'class':'form-control'})
        self.fields['talle'].widget.attrs.update({'class':'form-control'})
        self.fields['color'].widget.attrs.update({'class':'form-control'})
        self.fields['precio'].widget.attrs.update({'class':'form-control'})
        self.fields['genero'].widget.attrs.update({'class':'form-control'})

class FormuInvernal(forms.ModelForm):
    class Meta:
        model = Invernal
        fields = ["imagen","imagen_b","codigo","talle","color","precio","genero",]
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder':'Codigo(Requerido, Unico)'}),
            'talle': forms.TextInput(attrs={'placeholder':'Talle'}),
            'color': forms.TextInput(attrs={'placeholder':'Color'}),
            'precio': forms.TextInput(attrs={'placeholder':'Precio(Requerido)'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen_b'].widget.attrs.update({'class':'form-control'})
        self.fields['codigo'].widget.attrs.update({'class':'form-control'})
        self.fields['talle'].widget.attrs.update({'class':'form-control'})
        self.fields['color'].widget.attrs.update({'class':'form-control'})
        self.fields['precio'].widget.attrs.update({'class':'form-control'})
        self.fields['genero'].widget.attrs.update({'class':'form-control'})

class FormuPantalon(forms.ModelForm):
    class Meta:
        model = Pantalon
        fields = ["imagen","imagen_b","codigo","talle","color","precio","genero",]
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder':'Codigo(Requerido, Unico)'}),
            'talle': forms.TextInput(attrs={'placeholder':'Talle'}),
            'color': forms.TextInput(attrs={'placeholder':'Color'}),
            'precio': forms.TextInput(attrs={'placeholder':'Precio(Requerido)'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen_b'].widget.attrs.update({'class':'form-control'})
        self.fields['codigo'].widget.attrs.update({'class':'form-control'})
        self.fields['talle'].widget.attrs.update({'class':'form-control'})
        self.fields['color'].widget.attrs.update({'class':'form-control'})
        self.fields['precio'].widget.attrs.update({'class':'form-control'})
        self.fields['genero'].widget.attrs.update({'class':'form-control'})



class FormularioRegistro(UserCreationForm):
    password1 = forms.CharField(label='Ingrese contraseña:', widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}))
    password2 = forms.CharField(label=' Repita contraseña:', widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}))

    class Meta:

        model = User
        fields = ["username","password1","password2"]

class FormularioEditarUsuario(UserCreationForm):
    email = forms.EmailField(label='Ingrese email',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    first_name= forms.CharField(label='Ingrese nombre',widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    last_name= forms.CharField(label='Ingrese apellido',widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
    password1 = forms.CharField(label='Ingrese la contraseña', widget=forms.PasswordInput(attrs={'placeholder':'Nueva contraseña'}))
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput(attrs={'placeholder':'Repita contraseña'}))

    class Meta:

        model = User
        fields = ["first_name","last_name","email","password1","password2"]
