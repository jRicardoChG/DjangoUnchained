from django.db import models

# la app modelo la creare con el ejemplo de la tarea 2, la base de datos de la apgina de libros y las reviews
# esta base de datos tiene 3 tablas: usuarios, libros y reviews, mas adelante vere como asociar los regsitros de login de Django con esta base de datos 
# Create your models here.
# Requisitos: sudo pip3 install django psycopg2-binary
# para crear las tablas en la base de datos se debe:
# 1. Crear el modelo correctmaente en el archivo models.py
# 2. crear ma migracion django python3 manage.py makemigrations;  lo cual cre aun archivo xxxx_initial.py
# 3. con python3 manage.py sqlmigrate (nombre de la app que contiene el modelo) (numero de archivo initial.py); crea el codigo sql postgres
# 4. python3 manage.py migrate; ejecuta el codigo sql creado por django
# se puedencrear elelmentos en la base de datos usando la shell de django python3 manage.py shell
# codigos para crear:
# from App01.models import libros   <----tabla

#  
# f = libros(titulo = principito, autor=alguien,ISBN=1234567,fecha=hoy)
# f.save()
# encaso de existir tblas con llaves foraneas, los objetos de las demas tablas deben existir para que django los pueda asociar asi:
# sea f objeto de libros y g objeto de usuarios: r = reviews(dueno=g,libro=f)


class usuarios(models.Model):
    nombre = models.CharField(max_length=64)
    contrasena = models.CharField(max_length=64)

    def __str__(self):
        return f"user: {self.nombre},pass: ({self.contrasena})"

class libros(models.Model):
    titulo = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    ISBN = models.CharField(max_length=64)
    fecha = models.CharField(max_length=64)

    def __str__(self):
        return f"titulo: {self.titulo},autor: {self.autor},ISBN: {self.ISBN}, release: {self.fecha}"

class reviews(models.Model):
    dueno = models.ForeignKey(usuarios,on_delete=models.CASCADE, related_name="duenoReview")
    libro = models.ForeignKey(libros, on_delete=models.CASCADE, related_name="tituloLibro")
    review = models.CharField(max_length=256,null=True)

    def __str__(self):
        return f"REVIEW dueno: {self.dueno},libro: {self.libro}"


