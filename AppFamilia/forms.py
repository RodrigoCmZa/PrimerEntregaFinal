from django import forms

    # Create your models here.
class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fechaNacimiento = forms.DateField(null=True, blank=True)
    ocupacion = forms.CharField(max_length=30)
    class Meta():
        ordering = ('apellido', 'nombre') # Ordena.
        unique_together = ('nombre', 'apellido', 'edad', 'fechaNacimiento') # No permite que se repitan.
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def str(self) -> str:
       return f'{self.apellido}, {self.nombre}'
    # Muestra en la pagina del Admin "apellido, nombre"


class TareasForm(forms.Form):
    nombre = forms.CharField(max_length=30) 
    dia_de_creacion = forms.DateTimeField(null=True, blank=True)
    responsable = forms.CharField(max_length=30) 

    class Meta():
        ordering = ('dia_de_creacion', '-nombre', 'responsable') # Ordena.
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def str(self) -> str:
       return f'{self.nombre}'
    # Muestra en la pagina del Admin "apellido, nombre"


class HerramientasForm(forms.Forms):
    nombre = forms.CharField(max_length=30)
    tipo_de_tarea = forms.CharField(max_length=30)

    class Meta():
        ordering = ('nombre', 'tipo_de_tarea') # Ordena.
        verbose_name = 'Herramienta'
        verbose_name_plural = 'Herramientas'

    def str(self) -> str:
       return f'{self.nombre}'
    # Muestra en la pagina del Admin "apellido, nombre"