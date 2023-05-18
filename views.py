from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import json

def index(request):

    return HttpResponse("Hola Mundo")

class Inicio(View):
    template_name = "index.html"

    def post(self, request):
        return render(request)
    
    def get(self, request):
        nombres = "Julio Rafael"
        primer_apellido = "Sanchez"
        segundo_apellido = "Gaxiola"
        fecha_nacimiento = "30/06/1990"
        celular = "+52 3312395600"
        correo = "j.sanchezg7@hotmail.com"
        domicilio = "Toro 4851"
        genero = "Masculino"
        objetivo = "Gerente de Planeacion"
        salario = "$50,000 MXN"

        #todo el contenido aqui


        #hacer json aqui
        
        return render(request, self.template_name, {
            "nombres" : nombres, 
            "primer_apellido" : primer_apellido,
            "segundo_apellido" : segundo_apellido,
            "fecha_nacimiento" : fecha_nacimiento,
            "celular" : celular,
            "correo" : correo,
            "domicilio" : domicilio,
            "genero" : genero,
            "objetivo" : objetivo,
            "salario" : salario
 
        })
    


