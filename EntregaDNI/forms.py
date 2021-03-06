import datetime
from django import forms
from django.shortcuts import get_object_or_404
from . import models


class FormCaja(forms.ModelForm):

    class Meta:
        model = models.Caja
        fields = '__all__'
        widgets = {
                'codigo': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Código de caja'
                    }),
                'centro': forms.Select(attrs={'class': 'form-control'}),
                'cantidad': forms.NumberInput(attrs={'class': 'form-control'})
                }


class FormCentro(forms.ModelForm):

    class Meta:
        model = models.Centro
        fields = ('nombre',)
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control',
            'placeholder': 'Nombre del centro'})}


class FormSobre(forms.ModelForm):

    caja = forms.CharField(required=True, max_length=7, widget=forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Código QR de la caja', 'readonly': True}))

    class Meta:
        model = models.Sobre
        fields = ('codigo',)
        widgets = {
                'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código QR del sobre', 'readonly': True}),
        }

    def save(self, commit=True):
        """ Reescribe el método de guardar """

        cod_sobre = self.cleaned_data['codigo']
        cod_caja = self.cleaned_data['caja']

        caja = models.Caja.objects.get(codigo=cod_caja)
        nuevo_sobre = models.Sobre(codigo=cod_sobre)
        nuevo_sobre.caja = caja

        if commit:
            nuevo_sobre.save()

        return nuevo_sobre

    def clean_caja(self):
        """ Valida si la caja existe """

        caja = None
        cod_caja = codigo=self.cleaned_data['caja']
        caja = models.Caja.objects.filter(codigo=cod_caja)

        if not caja:
            raise forms.ValidationError('No se encuentra la caja en el sistema')
        
        return cod_caja


class FormSobreUsuario(FormSobre):
    """ Extensión de formulario de sobre que añade el usuario que entrega """

    class Meta(FormSobre.Meta):
        fields = FormSobre.Meta.fields + ('usuario',)
        widgets = FormSobre.Meta.widgets
        widgets['usuario'] = forms.Select(attrs={'class': 'form-control'})

    def save(self, commit=True):
        usuario = self.cleaned_data['usuario']
        nuevo_sobre = super().save(commit=False)
        nuevo_sobre.usuario = usuario

        if commit:
            usuario.save()

        return nuevo_sobre


class FormularioDomiciliaria(forms.ModelForm):
    """ Formulario para crear/editar domiciliarias """

    def __init__(self, edicion=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['hora_inicio'].input_formats = ('%I:%M %p',)
        self.fields['hora_final'].input_formats = ('%I:%M %p',)

        if not edicion:
            self.fields['integrantes'].queryset = models.Integrante.objects.exclude(sedes__fecha=datetime.date.today())

    class Meta:
        model = models.Domiciliarias
        fields = ('integrantes', 'hora_inicio', 'hora_final',)


        widgets = {
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control datetimepicker-input',
                                                  'placeholder': 'Hora de inicio',
                                                  'data-target': '#hora_inicio'}, format='%I:%M %p'),
            'hora_final': forms.TimeInput(attrs={'class': 'form-control datetimepicker-input',
                                                 'placeholder': 'Hora final',
                                                 'data-target': '#hora_final'}, format='%I:%M %p'),
            'integrantes': forms.SelectMultiple(attrs={'class': 'form-control'}),
            }
