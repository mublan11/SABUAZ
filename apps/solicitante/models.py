from django.db import models

SEX = (
    ('HOMBRE', 'HOMBRE'),
    ('MUJER', 'MUJER'),
)

STATUS_CHOICES = (
    ('ACEPTADA', 'ACEPTADA'),
    ('PENDIENTE', 'PENDIENTE'),
    ('RECHAZADA', 'RECHAZADA'),
)

PHONE_TYPE = (
    ('FIJO', 'FIJO'),
    ('CELULAR', 'CELULAR'),
)

BECA_CHOICES = (
    ('ALIMENTACION', 'ALIMENTACION'),
    ('HOSPEDAJE', 'HOSPEDAJE'),
    ('ALIMENTACION Y HOSPEDAJE', 'ALIMENTACION Y HOSPEDAJE'),
)
SOLICITUD = (
    ('RENOVACION', 'RENOVACION'),
    ('NUEVO INGRESO', 'NUEVO INGRESO'),
)




class UnidadAcademica(models.Model):
    nombre = models.CharField(u'nombre', max_length=70)

    def __str__(self):
        return self.nombre


class ProgramaLicenciatura(models.Model):
    nombre = models.CharField(u'nombre', max_length=70)
    # Foreign Keys
    unidad_academica_id = models.ForeignKey(UnidadAcademica, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class DatosAcademicos(models.Model):
    matricula = models.CharField(
        u'matricula', max_length=8, unique=True)
    promedio = models.FloatField(u'promedio')
    unidad_academica = models.ForeignKey(UnidadAcademica)
    programa_academico = models.ForeignKey(ProgramaLicenciatura)

    def __str__(self):
        return "{0} {1}".format(self.promedio, self.matricula)


class Telefono(models.Model):
    telefono = models.CharField(
        u'telefono', max_length=10)
    tipo = models.CharField(
        u'tipo', max_length=10, choices=PHONE_TYPE, default='FIJO')

    def __str__(self):
        return self.telefono


class Estado(models.Model):
    estado = models.CharField(
        u'estado', max_length=50, default='ZACATECAS')

    def __str__(self):
        return self.estado


class Municipio(models.Model):
    municipio = models.CharField(
        u'municipio', max_length=50)
    estado_fk = models.ForeignKey(Estado)

    def __str__(self):
        return self.municipio


class Domicilio(models.Model):
    numero = models.CharField(
        u'numero', max_length=6, null=True)
    calle = models.CharField(
        u'calle', max_length=50)
    colonia = models.CharField(
        u'colonia', max_length=50)
    codigo_postal = models.CharField(
        u'codigo_postal', max_length=5)
    estado = models.ForeignKey(Estado)
    municipio = models.ForeignKey(Municipio)

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5}".format(self.calle, self.numero, self.colonia,
            self. codigo_postal, self.estado, self.municipio)


class Documentos(models.Model):
    tipo_beca = models.CharField(max_length=25, choices=BECA_CHOICES)
    tipo_solicitud = models.CharField(max_length=25, choices=SOLICITUD)
    estudio_socioeconomico = models.FileField(upload_to='documentos/', null=True, blank=True)
    comprobante_ingresos = models.FileField(upload_to='documentos/', null=True, blank=True)
    ine_padres = models.FileField(upload_to='documentos/', null=True, blank=True)
    comprobante_inscripcion = models.FileField(upload_to='documentos/', null=True, blank=True)
    boleta_calificaciones = models.FileField(upload_to='documentos/', null=True, blank=True)
    carta_compromiso_padres = models.FileField(upload_to='documentos/', null=True, blank=True)
    comprobante_solicitud_linea = models.FileField(upload_to='documentos/', null=True, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.tipo_beca, self.tipo_solicitud)


class Solicitante(models.Model):
    nombre = models.CharField(
        u'nombre', max_length=50)
    apellido_paterno = models.CharField(
        u'apellido_paterno', max_length=50)
    apellido_materno = models.CharField(
        u'apellido_materno', max_length=50)
    sexo = models.CharField(
        u'sexo', max_length=10, choices=SEX)
    status = models.CharField(
        u'status', max_length=10, null=True, blank=True, choices=STATUS_CHOICES)
    # Foreign Keys
    datos_academicos_fk = models.ForeignKey(DatosAcademicos, on_delete=models.CASCADE, null=True)
    telefono_fk = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    domicilio_fk = models.ForeignKey(Domicilio, on_delete=models.CASCADE)
    documentos_fk = models.ForeignKey(Documentos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre