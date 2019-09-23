from django.db import models

# la app modelo la creare con el ejemplo de la tarea 2, la base de datos de la apgina de libros y las reviews
# esta base de datos tiene 3 tablas: usuarios, libros y reviews, mas adelante vere como asociar los regsitros de login de Django con esta base de datos 
# Create your models here.

class usuarios(models.model):
    nombre = models.CharField(max_length=64)
    contrasena = models.CharField(max_length=64)

    def __str__(self):
        return f"user: {self.nombre},pass: ({self.contrasena})"

class libros(models.model):
    titulo = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    ISBN = models.CharField(max_length=64)
    fecha = models.CharField(max_length=64)

    def __str__(self):
        return f"titulo: {self.titulo},autor: {self.autor},ISBN: {self.ISBN}, release: {self.fecha}"

class reviews(models.model):
    dueno = models.ForeignKey(usuarios,on_delete=models.CASCADE, related_name="duenoReview")
    libro = models.ForeignKey(libros, on_delete=models.CASCADE, related_name="tituloLibro")

    def __str__(self):
        return f"REVIEW dueno: {self.dueno},libro: {self.libro}"


