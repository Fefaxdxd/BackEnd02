from django.shortcuts import render

# Create your views here.
def art(request):
    return render(request,'templateDos/arte.html')

def visual(request):
    data={
        "banv":"imagenes/coon.png",
        "titulo":"Arte Visual",
        "dato1V":"Pintura al óleo",
        "dato2V":"Escultura en mármol",
        "dato3V":"Fotografía",
        "dato4V":"Arte callejero",
    }
    return render(request, 'templateDos/art.html',data)

def escenico(request):
    data={
        "bane":"imagenes/persa.jpg",
        "titulo":"Arte Escénico",
        "dato1E":"Teatro griego antiguo",
        "dato2E":"Danza contemporánea",
        "dato3E":"Ópera",
        "dato4E":"Teatro de marionetas"
    }
    return render(request, 'templateDos/art.html',data)

def literario(request):
    data={
        "banl":"imagenes/siames.webp",
        "titulo":"Arte Literario",
        "dato1L":"William Shakespeare",
        "dato2L":"Don Quijote de Cervantes",
        "dato3L":"Poesía",
        "dato4L":"Ensayos de Montaigne"
    }
    return render(request, 'templateDos/art.html',data)