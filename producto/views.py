from django.shortcuts import render



def index(request):
    return render(request, "producto/index_producto.html")

