from django.shortcuts import render

#Request es un diccionario que continuamente se va pasando entre el navegador y el servidor

def Home(request):
	return render(request, 'home.html')

def Nosotros(request):
	return render(request, 'nosotros.html')