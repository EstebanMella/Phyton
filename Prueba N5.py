#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
num_p_encuestadas = 0
j = 0 #variable para indicar la persona que se le ingresa la edad y sexo
cant_ninos=0
cant_joven=0
cant_adulto=0
cant_anciano=0
cant_femenino=0
cant_masculino =0
Femenino = "F"
Masculino = "M"

print "Ingrese cantidad de personas encuestadas"
num_p_encuestadas =  input()
while num_p_encuestadas < 0:#valida que el numero de personas sea igual o mayor a  0
	print "ingrese cantidad mayor o igual a 0"
	num_p_encuestadas =  input()
	


while j != num_p_encuestadas:
	j = j + 1
	print "Ingrese Edad persona Numero ",j, ": "
	edad_p_encuestada = input()
	while edad_p_encuestada < 0 and edad_p_encuestada>100:#valida si la edad esta entre el rango de 0 a 100
		print "ingrese edad entre 0 y 100"
		edad_p_encuestada = input()
	if edad_p_encuestada < 16: #revisa de que edad son las personas y las guarda segun corresponda
		cant_ninos = cant_ninos + 1
	elif edad_p_encuestada <26:
		cant_joven = cant_joven + 1
	elif edad_p_encuestada < 65:
		cant_adulto = cant_adulto +1 
	else:
		cant_anciano = cant_anciano +1
	print "Ingrese sexo persona F / M"
	sexo_p_encuestada = raw_input()
	while sexo_p_encuestada != Femenino and sexo_p_encuestada != Masculino: #valida si el sexo es f o m
		if sexo_p_encuestada == "f":
			sexo_p_encuestada = Femenino
		elif sexo_p_encuestada == "m":
			sexo_p_encuestada = Masculino
		else:
			print "Ingrese un sexo valido F/M"
			sexo_p_encuestada = raw_input()
		if sexo_p_encuestada == Femenino:
			cant_femenino = cant_femenino +1
		else:
			cant_masculino = cant_masculino +1

print "                       "
print "Cantidad de Ninos: ", cant_ninos
print "Cantidad de Jovenes: ", cant_joven
print "Cantidad de Adultos: ", cant_adulto
print "Cantidad de Ancianos: ", cant_anciano
print "               "
print "Cantidad de Mujeres: ", cant_femenino
print "Cantiad de Hombres: ", cant_masculino
		

	

	
	


