
# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request,'templateUno/index.html')

def electronica(request):
    data={
        "titulo":"Electronica",
        "producto1":"MC",
        "producto2":"Celular",
        "producto3":"Laptop",
        "imagen":"imagenes/producto.jpg"
    }
    return render(request, 'templateUno/productos.html',data)

def juguetes(request):
    data={
        "titulo":"Juguetes",
        "producto1":"Hotwheels",
        "producto2":"Pelota",
        "producto3":"yoyo"
    }
    return render(request, 'templateUno/productos.html',data)

def ropa(request):
    data={
        "titulo":"Ropa",
        "producto1":"Camisa",
        "producto2":"Playera",
        "producto3":"Pantalon"
    }
    return render(request, 'templateUno/productos.html',data)
