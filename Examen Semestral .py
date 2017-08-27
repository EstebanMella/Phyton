#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Estructuras de Programacion
# Proyecto Semestras
# Le Hote Le
# by: Esteban Mella
global lista_usuario
global lista_pass_usuario
lista_usuario= ["admin"]
lista_pass_usuario=["admin"]
opcion_usuario=0
contrasena_usuario="passs"
vol_m_login = True
vol_m_administrador=True
cant_desayuno=0
tematica=0
opcion_dia=0
global lista_cenas
lista_cenas=[]
global lista_pre_cenas
lista_pre_cenas=[]
global ingre_cenas
global lista_ingre_cenas
lista_ingre_cenas={}
ingre_cenas=[]
global lista_almuerzo
lista_almuerzo=[]
global lista_pre_almuerzos
lista_pre_almuerzos=[]
global ingre_almuerzos
global lista_ingre_almuerzos
lista_ingre_almuerzos={}
ingre_almuerzos=[]
global cant_desayuno
global lista_desayunos
global lista_pre_desayunos
global ingre_desayunos
global lista_ingre_desayunos
lista_ingre_desayunos ={}
ingre_desayunos=[]
lista_pre_desayunos=[]
lista_desayunos=[]
cant_desayuno=0
cant_almuerzos=0
cant_cenas=0

desayuno_mexico=["Huevos rancheros","Atole de guayaba","Chilaquiles con pollo"]
precio_mexico_desa=[6500,7000,5500]
ingre_mexico_desa={0:[ "jitomate","chile serrano"," diente de ajo. Sal y Pimienta, al gusto","Huevos","Tortillas","frijoles refritos"],1:["Trozo de canela","Cucharadas de fecula de maiz","Guayaba natural","Taza de agua para licuar las guayabas","Latas de leche evaporada","Pizca de bicarbonato"],2:["Kilo de jitomates","Chiles chipotle adobados","Carne de pollo, cocida y deshebrada","Taza de crema","Taza de queso Cotija rallado","Tazas de frijoles refritos","Arroz Frito"],2:["Merluza","Tomates rojos","Cebolla","Limas","Pimientos jalapeños"]}
almuerzo_mexico=["Tortillas mexicanas rellenas de carne","Mole con arroz","Ceviche de pescado mexicano"]
precio_mexico_almu=[10990,12990,15000]
ingre_mexico_almu={0:["Tortillas mexicanas","Carne picada","Guindilla (opcional)","Queso rallado","Tomate frito"],1:["Frasco de mole","Pechuga de pollo","Jitomates","Chile habanero","Onza de chocolate negro"],2:["Pescados blancos","Jugo de limon","Tomate rojo","Chile verde","Cebolla"]}
cena_mexico=["Enchiladas de pollo con queso","Sincronizadas mexicanas","Enfrijoladas de pollo con queso"]
precio_mexico_cena=[15900,14900,15900]
ingre_mexico_cena={0:["Pechuga de pollo","Tortillas de maíz","Zanahoria","Pimientos verdes","Queso Gauda"],1:["Tortillas mexicanas de trigo","Lonchas de queso semicurado","Lonchas de jamón cocido","Pimiento rojo","Hierbas secas (tomillo, orégano, salvia, perejil)"],2:["Tortillas de maíz","Pechugas de pollo","Alubias negras cocidas (frijoles)","Hojas de lechuga","Rabanitos"]}

desayuno_chile=["Sándwich Barros Luco","Sándwich Gran Chacarero","Sándwich Chilesandwich"]
precio_chile_desa=[2900,3900,4500]
ingre_chile_desa={0:["Carne a la plancha","Pan Blanco","Pan Integral","Queso Caliente","Pimienta y Sal a Gusto"],1:["Lomo cerdo","Palmito","Porotos verde","Pan amasado","Tomate"],2:["Pan Amasado","Lomo cerdo","Cebolla frita","Champiñón","Queso","Tomate"]}
almuerzo_chile=["Chupe de Locos","Pastel de Jaiba","Plateada al Jugo"]
precio_chile_almu=[11990,13000,14990]
ingre_chile_almu={0:["Locos","Panes (marraqueta)","Taza de leche","Cebolla","ramito de perejil"],1:["Jaiba (desmenuzada)","Huevos","Queso rallado","Cucharadas de vino ","Leche"]}
cena_chile=["Cazuela de Ave","Cazuela de Cordero","Pantrucas"]
precio_chile_cena=[13990,14990,15990]
ingre_chile_cena={0:["Trutros cortos de pollo","Pimentón verde","Papas","Trozos de zapallo","Trozos de choclo"],1:["Cordero","Papas","Arroz","Pimiento morrón","Porotos verdes "],2:["Harina","Dientes de ajo","Cebolla","Mantequilla","Tabletas de caldo de carne"]}

desayuno_peru=["Alfajores de Lima","Bizcochuelo al vapor","Budín de manzanas"]
precio_peru_desa=[3200,4000,3500]
ingre_peru_desa={0:["Harina","Yemas","Mantequilla","Azúcar en polvo","Sal"],1:["Claras","Azúcar","Yemas","Harina preparada"],2:["Bizcochuelo","Huevos","Azúcar en polvo","Puré de manzanas","Mantequilla","Pasas"]}
almuerzo_peru=["Ají de caiguas y pavita","Cebiche de lenguado","Chupe de camarones"]
precio_peru_almu=[12990,13990,14990]
ingre_peru_almu={0:["Chuletas de pavita deshuesadas","Ají amarillo molido","Ají panca molido","Papas amarillas","Choclo cocido"],1:["Filete de lenguado","Cebollas","Limones de Chulucanas","Ajo molido","Ají limo sin venas ni pepas"],2:["Cebolla roja","Ramas de huacatay","Camarones medianos","Zapallo lumina con cáscara","Queso de Lluta"]}
cena_peru=["Adobo arequipeño","Aguadito de conchas","Ají de atún al horno"]
precio_peru_cena=[14990,15990,16990]
ingre_peru_cena={0:["Pierna de cerd","Vinagre rojo","Chicha de jora","Granos de pimienta de chapa","crema de ají panca"],1:["Caldo de pescado","Papas amarillas","Ají amarillo molido","culantro molido","Arroz"],2:["Queso parmesano rallado","Leche evaporada","Atún","Crema de ají panca","Mantequilla"]}

#funcion Imprime el desayuno de peru ya dado el la lista
def imprimir_desayuno_peru():
	numero_de_platos=3
	x=0
	i=0
	print "-------------Desayunos----------"
	for i in range(0,numero_de_platos):
		print "Nombre: ", desayuno_peru[x]
		print "Precio: ", precio_peru_desa[x]
		print "Ingredientes: ", ingre_peru_desa[x]
		print " "
		x=x+1
		
#funcion Imprime el almuerzo de peru ya dado el la lista
def imprimir_almuerzo_peru():
	print "--------------Almuerzos-----------"
	numero_de_platos=3
	x=0
	i=0
	for i in range(0,numero_de_platos):
		total_precio=(precio_peru_almu[x]*1.15)
		print "Nombre: ", almuerzo_peru[x]
		print "Precio: ", total_precio
		print "Ingredientes: ", ingre_peru_almu[x]
		print " "
		x=x+1
	
#funcion Imprime la cena de peru ya dado el la lista
def imprimir_cena_peru():
	print "---------------Cenas--------------"
	numero_de_platos=3
	x=0
	i=0
	for i in range(0,numero_de_platos):
		total_precio=(precio_peru_cena[x]*1.15)
		print "Nombre: ", cena_peru[x]
		print "Precio: ", total_precio
		print "Ingredientes: ", ingre_peru_cena[x]
		print " "
		x=x+1

#funcion Imprime el desayuno de chile ya dado el la lista
def imprimir_desayuno_chile():
	numero_de_platos=3
	x=0
	i=0
	print "-------------Desayunos----------"
	for i in range(0,numero_de_platos):
		print "Nombre: ", desayuno_chile[x]
		print "Precio: ", precio_chile_desa[x]
		print "Ingredientes: ", ingre_chile_desa[x]
		print " "
		x=x+1

#funcion Imprime el almuerzo de chile ya dado el la lista
def imprimir_almuerzo_chile():
	print "--------------Almuerzos-----------"
	numero_de_platos=3
	x=0
	i=0
	for i in range(0,numero_de_platos):
		precio_total=(precio_chile_almu[x]*1.2)
		print "Nombre: ", almuerzo_chile[x]
		print "Precio: ", precio_total
		print "Ingredientes: ", ingre_chile_almu[x]
		print " "
		x=x+1
		
#funcion Imprime la cena de chile ya dado el la lista
def imprimir_cena_chile():
	print "---------------Cenas--------------"
	numero_de_platos=3
	x=0
	i=0
	for i in range(0,numero_de_platos):
		print "Nombre: ", cena_chile[x]
		print "Precio: ", precio_chile_cena[x]
		print "Ingredientes: ", ingre_chile_cena[x]
		print " "
		x=x+1	
	
#funcion Imprime el desayuno de mexico ya dado el la lista
def imprimir_desayuno_mexico():
	numero_de_platos=3
	x=0
	i=0
	print "-------------Desayunos----------"
	for i in range(0,numero_de_platos):
		precio_total=(precio_mexico_desa[x]*1.1)
		print "Nombre: ", desayuno_mexico[x]
		print "Precio: ", precio_total
		print "Ingredientes: ", ingre_mexico_desa[x]
		print " "
		x=x+1
#funcion Imprime el almuerzo de mexico ya dado el la lista
def imprimir_almuerzo_mexico():
	print "--------------Almuerzos-----------"
	numero_de_platos=3
	x=0
	i=0
	for i in range(0,numero_de_platos):
		print "Nombre: ", almuerzo_mexico[x]
		print "Precio: ", precio_mexico_almu[x]
		print "Ingredientes: ", ingre_mexico_almu[x]
		print " "
		x=x+1
		
#funcion Imprime la cena de mexico ya dado el la lista
def imprimir_cena_mexico():
	print "---------------Cenas--------------"
	numero_de_platos=3
	x=0
	i=0
	for i in range(0,numero_de_platos):
		print "Nombre: ", cena_mexico[x]
		print "Precio: ", precio_mexico_cena[x]
		print "Ingredientes: ", ingre_mexico_cena[x]
		print " "
		x=x+1
		
def limpiar_todo():
	for i in range(24):
		print " "

def menu_login_admin():
	print """	1)Login Menu Admin
	2)Agregar Administrador
	3)Salir"""
	opc_login_admin=input()
	while opc_login_admin<1 or opc_login_admin>3:
		print """	1)Login Menu Admin
	2)Agregar Administrador
	3)Salir"""
		opc_login_admin=input()
	if opc_login_admin==1:
		admin_login()
	if opc_login_admin==2:
		agregar_admin()
	if opc_login_admin==3:
		limpiar_todo()
		Inicio()
def agregar_admin():
	usuario= raw_input("Ingrese Usuario: ")
	longitud_prueba=len(lista_usuario)
	for i in range(longitud_prueba):
		comparar_usu=lista_usuario[i]
		if comparar_usu==usuario:
			print "El Usuario ya esta Registado"
			agregar_admin()
	print "Su Usuario es: ", usuario
	print "Esta Seguro 1)Si 2)No"
	opc_usuario=input()
	while opc_usuario!=1 and opc_usuario!=2:
		print "Su Usuario es: ", usuario
		print "Esta Seguro 1)Si 2)No"
		opc_usuario=input()
	while opc_usuario==2:
		print "Ingrese Usuario"
		usuario= raw_input()
		print "Su Usuario es: ", usuario
		print "Esta Seguro 1)Si 2)No"
		opc_usuario=input()
		while opc_usuario!=1 and opc_usuario!=2:
			print "Su Usuario es: ", usuario
			print "Esta Seguro 1)Si 2)No"
			opc_usuario=input()
	print "Ingrese Su Password"
	pass_usuario=raw_input()
	print "Su Password es: ", pass_usuario
	print "Esta Seguro 1)Si 2)No"
	opc_pass_usuario=input()
	while opc_pass_usuario!=1 and opc_pass_usuario!=2:
		print "Su Password es: ", pass_usuario
		print "Esta Seguro 1)Si 2)No"
		opc_pass_usuario=input()
	while opc_pass_usuario==2:
		print "Ingrese Usuario"
		pass_usuario= raw_input()
		print "Su Password es: ", pass_usuario
		print "Esta Seguro 1)Si 2)No"
		opc_pass_usuario=input()
		while opc_pass_usuario!=1 and opc_pass_usuario!=2:
			print "Su Password es: ", pass_usuario
			print "Esta Seguro 1)Si 2)No"
			opc_pass_usuario=input()
	longitud_usuario=len(lista_usuario)
	longitud_pass=len(lista_pass_usuario)
	lista_usuario.insert(longitud_usuario,usuario)
	lista_pass_usuario.insert(longitud_usuario,pass_usuario)
	menu_login_admin()
	
#funcion para el login del administrador con su usuario y pass
def admin_login():	
	salir=False
	while salir==False:		
		print "Si desea salir, escriba salir"
		usuario_ingre=raw_input("ingrese Usuario: ")
		nueva_line()
		longitud_usu=len(lista_usuario)-1
		x=0
		if usuario_ingre=="salir":
			menu_login_admin()
		while longitud_usu>=x:
			usuario=lista_usuario[x]
			if usuario==usuario_ingre:
				salir=True
			x=x+1
		x=x-1
		pass_usuario=lista_pass_usuario[x]
		while salir==True:
			print "Recuerde mayusculas diferente de minusculas"
			contrasena_usuario=raw_input("Ingrese Contraseña: ")
			usuario_ingre="salir"
			nueva_line()
			while contrasena_usuario!=pass_usuario:
				print "Recuerde mayusculas diferente de minusculas"
				contrasena_usuario=raw_input("Ingrese Contraseña Valida: ")
				usuario_ingre="salir"
				nueva_line()
			if contrasena_usuario==pass_usuario:
				menu_admin()

#funcion para crear un espacio
def nueva_line():
	print "  "	
	
#funcion para ver el menu del administrado una ves ingresado el usuario y pass. despues llama a sus sub funciones	
def menu_admin():
	
					print """Menu Adinistrador
		1)Dia a Modificar
		2)Modificar Menu  Completo
		3)Modificar Desayunos
		4)Modificar Almuerzos
		5)Modificar Cenas
		6)Revisar Menu
		7)Salir"""
					
					opc_administrador=input()
					nueva_line()
					while opc_administrador<1 or opc_administrador>7:
						print """Menu Adinistrador
		1)Dia a Modificar
		2)Modificar Menu  Completo
		3)Modificar Desayunos
		4)Modificar Almuerzos
		5)Modificar Cenas
		6)Ver  Menu
		7)Salir"""  
		
						opc_administrador=input("Ingrese Opcion Valida: ")
						nueva_line()
					if opc_administrador ==1:
						dia_modificar()
					if opc_administrador ==2 or opc_administrador==3 or opc_administrador == 4 or opc_administrador == 5:
						if opcion_dia== 1 or opcion_dia==3 or opcion_dia==6:
							print "Lo siento No se puede Modificar el dia"
							print "Tiene Tematica y menu ya prefijo"
							nueva_line()
							menu_admin()
					if opc_administrador == 2 and opcion_dia == 0:
						print "Necesita Ingresar Dia Primero Para Modificar Menu"
						nueva_line()
						dia_modificar()
					if opc_administrador==3 and opcion_dia==0:
						print "Necesita Ingresar Dia Primero Para Modificar Menu"
						nueva_line()
						dia_modificar()
					if opc_administrador == 4 and opcion_dia == 0:
						print "Necesita Ingresar Dia Primero Para Modificar Menu"
						nueva_line()
						dia_modificar()
					if opc_administrador == 5 and opcion_dia == 0:
						print "Necesita Ingresar Dia Primero Para Modificar Menu"
						nueva_line()
						dia_modificar()
					elif opc_administrador ==2 and opcion_dia != 0:
						Tematica()
						capturar_desayunos()
						capturar_almuerzo()
						capturar_cena()
						menu_admin()
					if opc_administrador ==3 and opcion_dia != 0:
						if tematica == "":
							Tematica()
						else:
							print "Menu para modificar Desayunos"
							Menu_modificar_desayuno()
					if opc_administrador ==4 and opcion_dia != 0:
						if tematica == "":
							Tematica()
						else:
							print "Menu para modificar Almuerzos"
							nueva_line()
							Menu_modificar_almuerzo()
					if opc_administrador ==5 and opcion_dia != 0:
						if tematica == "":
							Tematica()
						elif tematica!="" and opc_administrador==5:
							print "Menu para modificar Cenas"
							nueva_line()
							Menu_modificar_cena()
					if opcion_dia ==0:
						nueva_line()
						print "Primero Ingrese Menu"
						menu_admin()
					if opc_administrador == 6:
						if opcion_dia==2:
							imprimir_menu_desayuno()
							imprimir_menu_almuerzo()
							imprimir_menu_cena()
							nueva_line()
							menu_admin()
						if opcion_dia==4:
							imprimir_menu_desayuno()
							imprimir_menu_almuerzo()
							imprimir_menu_cena()
							nueva_line()
							menu_admin()
						if opcion_dia==5:
							imprimir_menu_desayuno()
							imprimir_menu_almuerzo()
							imprimir_menu_cena()
							nueva_line()
							menu_admin()
						if opcion_dia==7:
							imprimir_menu_desayuno()
							imprimir_menu_almuerzo()
							imprimir_menu_cena()
							nueva_line()
							menu_admin()
					if opc_administrador == 6:
						if opcion_dia==1:
							imprimir_desayuno_mexico()
							imprimir_almuerzo_mexico()
							imprimir_cena_mexico()
							nueva_line()
							menu_admin()
						if opcion_dia==3:
							imprimir_desayuno_chile()
							imprimir_almuerzo_chile()
							imprimir_cena_chile()
							nueva_line()
							menu_admin
						if opcion_dia==6:
							imprimir_desayuno_peru()
							imprimir_almuerzo_peru()
							imprimir_cena_peru()
							nueva_line()
							menu_admin()
					if opc_administrador==7:
						if opcion_dia ==0:
							print "Ingrese Primero Un menu"
							menu_admin()
						if opcion_dia==1 or opcion_dia ==3 or opcion_dia==6:
								Inicio()
						if opcion_dia!=1 or opcion_dia !=3 or opcion_dia!=6:
							if cant_almuerzos <3 and cant_desayuno<3 and cant_cenas<3:
								print "No Puede salir hasta que el menu tenga 3 desayuno, 3 almuerzos y 3 cenas como minimo"
								menu_admin()
						if cant_almuerzos >3 and cant_desayuno>3 and cant_cenas>3:
							Inicio()

#funcion para agregar tematica a los dias que no tengan		
def Tematica():
	tematica =""
	print "Ingrese Tematica"
	tematica = raw_input()
	nueva_line()			
				
#funcion para que te ingrese 3 o mas almuerzos o borrar todos e ingresarlos denuevo				
def capturar_almuerzo():
	global cant_almuerzos
	if opcion_dia == 2:
		print "Modificar Almuerzos del Dia Martes"
	if opcion_dia == 4:
		print "Modificar Almuerzos del Dia Jueves"
	if opcion_dia == 5:
		print "Modificar Almuerzos del Dia Viernes"
	if opcion_dia == 7:
		print "Modificar Almuerzos del Dia Domingo"
	print "Cuantos Almuerzos colocara?. Minimo 3"
	cant_almuerzos=input()
	while cant_almuerzos<3:
		print "Necesita Ingresar 3 o mas desayunos"
		cant_amuerzo=input()
		nueva_line()
	for i in range(0,cant_almuerzo):
		j=j+1
		print "Ingrese Nombre Almuerzo Numero ", j," del Menu"
		elemento=raw_input()
		nueva_line()
		lista_almuerzo.insert(i,elemento)
	for i2 in range(0,cant_almuerzos):
		print "Ingrese Precio Almuerzo ", lista_desayunos[i2]
		precio_almuerzo=input()
		nueva_line()
		while precio_almuerzo<0:
			print "Ingrese Precio mayor a 0"
			precio_almuerzo=input()
			nueva_line()
		lista_pre_almuerzos.insert(i2,precio_almuerzo)
	i3=True
	x=0
	while i3 ==True:
		print "Ingrese Numero de Ingredientes desayuno ", lista_desayunos[x]
		print "5 Ingresientes minimo"
		cant_ingredientes=input()
		nueva_line()
		while cant_ingredientes<5:
			print "Ingrese 5 o mas ingredientes"
			cant_ingredientes=input()
			nueva_line()
		for i4 in range(0,cant_ingredientes):
			print "Ingrese Ingrediente Numero: ", i4
			elemento=raw_input()
			nueva_line()
			ingre_almuerzos.insert(i4,elemento)
		lista_ingre_almuerzos[x]=ingre_desayunos
		x=x+1
		if x==cant_desayuno:
			i3=False

	
#funcion para crear el menu que nodifique un desayuno
def Menu_modificar_desayuno():
	global opc_modificar
	print """	1)Modificar menu completo
	2)Agregar 
	3)Borrar
	4)Salir"""
	opc_modificar=input()
	nueva_line()
	while opc_modificar<1 or opc_modificar >4:
		nueva_line()
		print "escoja una opcion valida"
		print """	1)Modificar menu completo
	2)Agregar 
	3)Borrar
	4)Salir"""
		opc_modificar=input()
	if opc_modificar==1:
		capturar_desayunos()
		menu_admin()
	if opc_modificar==4:
		menu_admin()
	if opc_modificar==2:
		if opcion_dia==2:
			agredar_desayuno()
			Menu_modificar_desayuno()
	if opc_modificar ==3:
		x=1
		i=0
		longitud=len(lista_desayunos)
		while longitud > i:
			print x,") Nombre: ", lista_desayunos[i]
			nueva_line()
			x=x+1
			i=i+1
		opc_borrar=input("Que numero desea borrar: ")
		while opc_borrar<1 or opc_borrar >x:
			print "Ingrese una opcion igual a 1 y que no supere a ",x
			opc_borrar = input()
		nueva_line()
		opc_borrar = opc_borrar - 1
		del lista_desayunos[opc_borrar]
		del lista_ingre_desayunos[opc_borrar]
		del lista_pre_desayunos[opc_borrar]
		x=1
		i=0
		longitud=len(lista_desayunos)
		while longitud > i:
			print x,") Nombre: ", lista_desayunos[i]
			nueva_line()
			x=x+1
			i=i+1
		nueva_line()
		Menu_modificar_desayuno()
	
#funcion para agregar un desayuno a la lista con su Nomre, precio yingredientes			
def agredar_desayuno():
	longitud=len(lista_desayunos)
	longitud = int(longitud)
	if longitud==0:
		cant_desayuno=longitud
	else:
		cant_desayuno=longitud+1
	print "Ingrese Nombre desayuno "
	elemento=raw_input()
	nueva_line()
	lista_desayunos.insert(cant_desayuno,elemento)
	print "Ingrese Precio desayuno ", lista_desayunos[cant_desayuno]
	precio_desayuno=input()
	nueva_line()
	while precio_desayuno<0:
		print "Ingrese Precio mayor a 0"
		precio_desayuno=input()
		nueva_line()
	lista_pre_desayunos.insert(cant_desayuno,precio_desayuno)
	print "Ingrese Numero de Ingredientes desayuno ", lista_desayunos[cant_desayuno]
	print "5 Ingresientes minimo"
	cant_ingredientes=input()
	while cant_ingredientes<5:
		print "Ingrese 5 o mas ingredientes"
		cant_ingredientes=input()
	j=0
	for i4 in range(0,cant_ingredientes):
		j=j+1
		print "Ingrese Ingrediente Numero: ", j
		elemento=raw_input()
		nueva_line()
		ingre_desayunos.insert(cant_desayuno,elemento)
	lista_ingre_desayunos[cant_desayuno]=ingre_desayunos

#funcion para agregar un menu que modifique un almuerzo
def Menu_modificar_almuerzo():
	global opc_modificar
	print """	1)Modificar menu completo
	2)Agregar 
	3)Borrar
	4)Salir"""
	opc_modificar=input()
	nueva_line()
	while opc_modificar<1 or opc_modificar >4:
		nueva_line()
		print "escoja una opcion valida"
		print """	1)Modificar menu completo Almuerzo
	2)Agregar 
	3)Borrar
	4)Salir"""
		opc_modificar=input()
	if opc_modificar==1:
		capturar_almuerzo()
		menu_admin()
	if opc_modificar==4:
		menu_admin()
	if opc_modificar==2:
		if opcion_dia==2:
			agredar_almuerzo()
			Menu_modificar_almuerzo()
	if opc_modificar ==3:
		x=1
		i=0
		longitud=len(lista_almuerzo)
		while longitud > i:
			print x,") Nombre: ", lista_almuerzo[i]
			nueva_line()
			x=x+1
			i=i+1
		opc_borrar=input("Que numero desea borrar: ")
		while opc_borrar<1 or opc_borrar >x:
			print "Ingrese una opcion igual a 1 y que no supere a ",x
			opc_borrar = input()
		nueva_line()
		opc_borrar = opc_borrar - 1
		del lista_almuerzo[opc_borrar]
		del lista_ingre_almuerzos[opc_borrar]
		del lista_pre_almuerzos[opc_borrar]
		x=1
		i=0
		longitud=len(lista_almuerzo)
		while longitud > i:
			print x,") Nombre: ", lista_almuerzo[i]
			nueva_line()
			x=x+1
			i=i+1
		nueva_line()
		Menu_modificar_almuerzo()


#funcion para agregar un almuerzo a la lista con su Nomre, precio yingredientes		
def agredar_almuerzo():
	longitud=len(lista_almuerzo)
	longitud = int(longitud)
	if longitud==0:
		cant_almuerzos=longitud
	else:
		cant_almuerzos=longitud+1
	print "Ingrese Nombre Almuerzo "
	elemento=raw_input()
	nueva_line()
	lista_almuerzo.insert(cant_almuerzos,elemento)
	print "Ingrese Precio Almuerzo ", lista_almuerzo[cant_almuerzos]
	precio_amuerzo=input()
	nueva_line()
	while precio_almuerzo<0:
		print "Ingrese Precio mayor a 0"
		precio_almuerzo=input()
		nueva_line()
	lista_pre_almuerzos.insert(cant_almuerzos,precio_almuerzo)
	print "Ingrese Numero de Ingredientes del Almuerzo ", lista_almuerzo[cant_almuerzos]
	print "5 Ingresientes minimo"
	cant_ingredientes=input()
	while cant_ingredientes<5:
		print "Ingrese 5 o mas ingredientes"
		cant_ingredientes=input()
	j=0
	for i4 in range(0,cant_ingredientes):
		j=j+1
		print "Ingrese Ingrediente Numero: ", j
		elemento=raw_input()
		nueva_line()
		ingre_almuerzos.insert(cant_almuerzos,elemento)
	lista_ingre_almuerzos[cant_almuerzos]=ingre_almuerzos

#funcion para cear el menu para modificar una cena
def Menu_modificar_cena():
	global opc_modificar
	print """	1)Modificar menu completo
	2)Agregar 
	3)Borrar
	4)Salir"""
	opc_modificar=input()
	nueva_line()
	while opc_modificar<1 or opc_modificar >4:
		nueva_line()
		print "escoja una opcion valida"
		print """	1)Modificar menu completo
	2)Agregar 
	3)Borrar
	4)Salir"""
		opc_modificar=input()
	if opc_modificar==1:
		capturar_cena()
		menu_admin()
	if opc_modificar==4:
		menu_admin()
	if opc_modificar==2:
		if opcion_dia==2:
			agredar_cena()
			Menu_modificar_cena()
	if opc_modificar ==3:
		x=1
		i=0
		longitud=len(lista_cenas)
		while longitud > i:
			print x,") Nombre: ", lista_cenas[i]
			nueva_line()
			x=x+1
			i=i+1
		opc_borrar=input("Que numero desea borrar: ")
		while opc_borrar<1 or opc_borrar >x:
			print "Ingrese una opcion igual a 1 y que no supere a ",x
			opc_borrar = input()
		nueva_line()
		opc_borrar = opc_borrar - 1
		del lista_cenas[opc_borrar]
		del lista_ingre_cenas[opc_borrar]
		del lista_pre_cenas[opc_borrar]
		x=1
		i=0
		longitud=len(lista_cenas)
		while longitud > i:
			print x,") Nombre: ", lista_cenas[i]
			nueva_line()
			x=x+1
			i=i+1
		nueva_line()
		Menu_modificar_cena()
	
#funcion para agregar una cena a la lista con su Nomre, precio yingredientes			
def agredar_cena():
	longitud=len(lista_cenas)
	longitud = int(longitud)
	if longitud==0:
		cant_cenas=longitud
	else:
		cant_cenas=longitud+1
	print "Ingrese Nombre de la Cena "
	elemento=raw_input()
	nueva_line()
	lista_cenas.insert(cant_cenas,elemento)
	print "Ingrese Precio de la Cena ", lista_cenas[cant_cenas]
	precio_cenas=input()
	nueva_line()
	while precio_cenas<0:
		print "Ingrese Precio mayor a 0"
		precio_cenas=input()
		nueva_line()
	lista_pre_cenas.insert(cant_cenas,precio_cenas)
	print "Ingrese Numero de Ingredientes de la Cena ", lista_cenas[cant_cenas]
	print "5 Ingresientes minimo"
	cant_ingredientes=input()
	while cant_ingredientes<5:
		print "Ingrese 5 o mas ingredientes"
		cant_ingredientes=input()
	j=0
	for i4 in range(0,cant_ingredientes):
		j=j+1
		print "Ingrese Ingrediente Numero: ", j
		elemento=raw_input()
		nueva_line()
		ingre_cenas.insert(cant_cenas,elemento)
	lista_ingre_cenas[cant_cenas]=ingre_cenas
		
#funcion para que te ingrese 3 o mas cenas o borrar todos e ingresarlos denuevo	
def capturar_cena():
	global cant_cenas
	if opcion_dia == 2:
		print "Modificar Cenas del Dia Martes"
	if opcion_dia == 4:
		print "Modificar Cenas del Dia Jueves"
	if opcion_dia == 5:
		print "Modificar Cenas del Dia Viernes"
	if opcion_dia == 7:
		print "Modificar Cenas del Dia Domingo"
	print "Cuantas Cenas colocara?. Minimo 3"
	cant_cenas=input()
	nueva_line()
	while cant_cenas<3:
		print "Necesita Ingresar 3 o mas Cenas"
		cant_cenas=input()
		nueva_line()
	j=0
	for i in range(0,cant_cenas):
		j=j+1
		print "Ingrese Nombre Cena Numero ", j," del Menu"
		elemento=raw_input()
		nueva_line()
		lista_cenas.insert(i,elemento)
	for i2 in range(0,cant_cenas):
		print "Ingrese Precio Cena ", lista_cenas[i2]
		precio_cenas=input()
		nueva_line()
		while precio_cenas<0:
			print "Ingrese Precio mayor a 0"
			precio_cenas=input()
			nueva_line()
		lista_pre_cenas.insert(i2,precio_cenas)
	i3=True
	x=0
	j=0
	while i3 ==True:
		print "Ingrese Numero de Ingredientes Cenas ", lista_cenas[x]
		print "5 Ingresientes minimo"
		cant_ingredientes=input()
		nueva_line()
		while cant_ingredientes<5:
			print "Ingrese 5 o mas ingredientes"
			cant_ingredientes=input()
		for i4 in range(0,cant_ingredientes):
			j=j+1
			print "Ingrese Ingrediente Numero: ", j
			elemento=raw_input()
			nueva_line()
			ingre_cenas.insert(i4,elemento)
		lista_ingre_cenas[x]=ingre_cenas
		x=x+1
		if x==cant_cenas:
			i3=False

#funcion para crear el menu para modificar un dia 		
def dia_modificar():
	global opcion_dia
	global opcion_dia_escojer
	while True:
			print """Escoja dia a Modificar
			1)Lunes
			2)Martes
			3)Miercoles
			4)Jueves
			5)Viernes
			6)Sabado
			7)Domingo
			8)Salir
			"""
			opcion_dia_escojer=input()
			nueva_line()
			while opcion_dia_escojer<1 or opcion_dia_escojer > 8:
				print """Escoja dia a Modificar valido:
			1)Lunes
			2)Martes
			3)Miercoles
			4)Jueves
			5)Viernes
			6)Sabado
			7)Domingo
			8)Salir
			"""
				opcion_dia_escojer=input("Ingrese Opcion Valida")
				nueva_line()
			if opcion_dia_escojer == 8:
				menu_admin()
			if opcion_dia_escojer>=1 and opcion_dia_escojer<=7:
				opcion_dia=opcion_dia_escojer
			if opcion_dia == 1:
				print """ Recuerde dia Lunes "Viva Mexico", donde la comida sera exclusivamente mexicana y tendrán un 10 porciento sobre el desayuno.	
			"""
				nueva_line()
				menu_admin()
			if opcion_dia == 3 :
				print """ Recuerde dia Miercoles "Viva Chile", donde la comida sera exclusivamente nacional y tendrán un 20 porciento sobre el precio del almuerzo.
			 """
				nueva_line()
				menu_admin()
			if opcion_dia == 6:
				print """ Recuerde día Sabado "Viva el Peru", donde la comida sera exclusivamente peruana y tendran un 15 porciento sobre el precio de la cena y almuerzo.
			"""
				nueva_line()
				menu_admin()
			if opcion_dia == 2 or opcion_dia==4 or opcion_dia == 5 or opcion_dia==7:
				print " Puede ingresar la tematica que quiera y el menu igual"
				print "Desea Modificar Menu Completo"
				print "1)Si"
				print "2)No"
				if opcion_dia_escojer>=1 and opcion_dia_escojer<=7:
					opcion_dia = opcion_dia_escojer
				opc_modif_menu_comple=input()
				nueva_line()
				while opc_modif_menu_comple<1 or opc_modif_menu_comple>2:
					print "ingrese opcion valida: "
					print "Desea Modificar Menu Completo"
					print "1)Si"
					print "2)No"
					opc_modif_menu_comple=input()
					nueva_line()
				if opc_modif_menu_comple== 1:
					Tematica()
					capturar_desayunos()
					capturar_almuerzo()
					capturar_cena()
					Inicio()
				else:
					dia_modificar()
					
#Imprime el desayuno de los dias que no tengan tematica, previamente agregados a la lista
def imprimir_menu_desayuno():
	if opcion_dia==0:
		print "Necesita Ingesar un menu Primero"
		menu_admin()
		nueva_line()
	print "+++++Menu Le Hote Le+++++"
	print "--------Desayunos--------"
	if opcion_dia!=1 and opcion_dia!=3 and opcion_dia!=6:
		longitud=len(lista_desayunos)
		x=0
		i=0
		while longitud>x:
			print "Nombre: ", lista_desayunos[x]
			print "Precio: ", lista_pre_desayunos[x]
			print "Ingredientes: ", lista_ingre_desayunos[x]
			nueva_line()
			x=x+1
		
#Imprime el almuerzo de los dias que no tengan tematica, previamente agregados a la lista
def imprimir_menu_almuerzo():
	if opcion_dia==0:
		print "Necesita Ingesar un menu Primero"
		menu_admin()
		nueva_line()
	print "+++++Menu Le Hote Le+++++"
	print "--------Amuerzo--------"
	if opcion_dia!=1 and opcion_dia!=3 and opcion_dia!=6:
		longitud=len(lista_almuerzo)
		x=0
		i=0
		while longitud > x:
			print "Nombre: ", lista_almuerzo[x]
			print "Precio: ", lista_pre_almuerzos[x]
			print "Ingredientes: ", lista_ingre_almuerzos[x]
			nueva_line()
			x=x+1		

#Imprime la cena de los dias que no tengan tematica, previamente agregados a la lista
def imprimir_menu_cena():
	if opcion_dia==0:
		print "Necesita Ingesar un menu Primero"
		menu_admin()
		nueva_line()
	print "+++++Menu Le Hote Le+++++"
	print "--------Amuerzo--------"
	if opcion_dia!=1 and opcion_dia!=3 and opcion_dia!=6:
		longitud=len(lista_cenas)
		x=0
		i=0
		while longitud > x:
			print "Nombre: ", lista_cenas[x]
			print "Precio: ", lista_pre_cenas[x]
			print "Ingredientes: ", lista_ingre_cenas[x]
			nueva_line()
			x=x+1	
			
			
#funcion para iniciar y llamar a las que sigen
def Inicio():

	print """		****************************
		******** Le Hote Le ********
		****************************
		"""
	print """Menu Principal
		Escoja Usuario
		1) Administrador
		2) Cliente 	"""
	opcion_usuario=input()
	while opcion_usuario<1 or opcion_usuario>2:
			print """Escoja Usuario valido
			1) Administrador
			2) Cliente 	"""
			opcion_usuario=input()
			nueva_line()
	if opcion_usuario ==1:
		menu_login_admin()
	if opcion_usuario==2:
		if opcion_dia==0:
			print "El Administrador no a puesto Menu"
			Inicio()
		else:
			menu_cliente()
	
#funcion para que te ingrese 3 o mas desayunos o borrar todos e ingresarlos denuevo		
def capturar_desayunos():
	global cant_desayuno
	if opcion_dia == 2 or opcion_dia_escojer == 2:
		print "Modificar Desayunos del Dia Martes"
	if opcion_dia == 4 or opcion_dia_escojer == 4:
		print "Modificar Desayunos del Dia Jueves"
	if opcion_dia == 5 or opcion_dia_escojer == 5:
		print "Modificar Desayunos del Dia Viernes"
	if opcion_dia == 7 or opcion_dia_escojer == 7:
		print "Modificar Desayunos del Dia Domingo"
		print "Cuantos desayunos colocara?. Minimo 3"
		cant_desayuno=input()
		nueva_line()
	while cant_desayuno<3:
		print "Necesita Ingresar 3 o mas desayunos"
		cant_desayuno=input()
		nueva_line()

	j=0
	for i in range(0,cant_desayuno):
		j=j+1
		print "Ingrese Nombre desayuno Numero ", j," del Menu"
		elemento=raw_input()
		nueva_line()
		lista_desayunos.insert(i,elemento)
	global lista_pre_desayunos
	lista_pre_desayunos=[]
	for i2 in range(0,cant_desayuno):
		print "Ingrese Precio desayuno ", lista_desayunos[i2]
		precio_desayuno=input()
		nueva_line()
		while precio_desayuno<0:
			print "Ingrese Precio mayor a 0"
			precio_desayuno=input()
			nueva_line()
		lista_pre_desayunos.insert(i2,precio_desayuno)
	global ingre_desayunos
	global lista_ingre_desayunos
	lista_ingre_desayunos={}
	ingre_desayunos=[]
	i3=True
	x=0
	while i3 ==True:
		print "Ingrese Numero de Ingredientes desayuno ", lista_desayunos[x]
		print "5 Ingresientes minimo"
		cant_ingredientes=input()
		while cant_ingredientes<5:
			print "Ingrese 5 o mas ingredientes"
			cant_ingredientes=input()
		j=0
		for i4 in range(0,cant_ingredientes):
			j=j+1
			print "Ingrese Ingrediente Numero: ", j
			elemento=raw_input()
			nueva_line()
			ingre_desayunos.insert(i4,elemento)
		lista_ingre_desayunos[x]=ingre_desayunos
		x=x+1
		if x==cant_desayuno:
			i3=False
	
#menu para el cliente no tiene clave. y llama a sus sub funciones dependiendo lo escojido
#la unica regla es que el administrador aya colocado un menu para ingresar, pero esta en el Inicio esa pregunta
def menu_cliente():
	nueva_line()
	print"""	Menu Cliente
	1) Ver menu Completo
	2) Ver Desayunos
	3) Ver Almuerzos
	4) Ver Cenas
	5) Buscar por Nombre
	6) Buscar por Precio Mayor
	7) Buscar por Precio Menor
	8) Salir
	"""	
	opc_cliente=input()
	while opc_cliente <1 or opc_cliente > 8:
		print "Ingrese Una opcion Valida:"
		print"""	Menu Cliente
	1) Ver menu Completo
	2) Ver Desayunos
	3) Ver Almuerzos
	4) Ver Cenas
	5) Buscar por Nombre
	6) Buscar por Precio Mayor
	7) Buscar por Precio Menor
	8) Salir
	"""	
		opc_cliente=input()
	if opc_cliente==8:
		Inicio()
	if opc_cliente ==1:
		if opcion_dia==2 or opcion_dia==4 or opcion_dia==5 or opcion_dia==7:
			imprimir_menu_desayuno()
			imprimir_menu_almuerzo()
			imprimir_menu_cena()
			menu_cliente()
		if opcion_dia==1:
			imprimir_desayuno_mexico()
			imprimir_almuerzo_mexico()
			imprimir_cena_mexico()
			menu_cliente()
		if opcion_dia==3:
			imprimir_desayuno_chile()
			imprimir_almuerzo_chile()
			imprimir_cena_chile()
			menu_cliente()
		if opcion_dia==6:
			imprimir_desayuno_peru()
			imprimir_almuerzo_peru()
			imprimir_cena_peru()
			menu_cliente()
	if opc_cliente ==2:
		if opcion_dia==2 or opcion_dia==4 or opcion_dia==5 or opcion_dia==7:
			imprimir_menu_desayuno()
			menu_cliente()
		if opcion_dia==1:
			imprimir_desayuno_mexico()
			menu_cliente()
		if opcion_dia==3:
			imprimir_desayuno_chile()
			menu_cliente()
		if opcion_dia==6:
			imprimir_desayuno_peru()
			menu_cliente()
	if opc_cliente ==3:
		if opcion_dia==2 or opcion_dia==4 or opcion_dia==5 or opcion_dia==7:
			imprimir_menu_almuerzo()
			menu_cliente()
		if opcion_dia==1:
			imprimir_almuerzo_mexico()
			menu_cliente()
		if opcion_dia==3:
			imprimir_almuerzo_chile()
			menu_cliente()
		if opcion_dia==6:
			imprimir_almuerzo_peru()
			menu_cliente()
	if opc_cliente ==4:
		if opcion_dia==2 or opcion_dia==4 or opcion_dia==5 or opcion_dia==7:
			imprimir_menu_cena()
			menu_cliente()
		if opcion_dia==1:
			imprimir_cena_mexico()
			menu_cliente()
		if opcion_dia==3:
			imprimir_cena_chile()
			menu_cliente()
		if opcion_dia==6:
			imprimir_cena_peru()
			menu_cliente()
	if opc_cliente==5:
		buscar_nombre()
	if opc_cliente==6:
		buscar_precio_mayor()
	if opc_cliente==7:
		buscar_precio_menor()
#funcion para buscar por nombre del plato
def buscar_nombre():
	print "Ingrese Nombre del Plato"
	buscar_nom=raw_input()
	if opcion_dia==2 or opcion_dia==4 or opcion_dia==5 or opcion_dia==7:
		longitud=len(lista_desayunos)
		longitud2=len(lista_almuerzo)
		longitud3=len(lista_cenas)
		x=0
		buscar_lista_desa=[]
		buscar_lista_almu=[]
		buscar_lista_cena=[]
		while longitud > x:
			res_nom=lista_desayunos[x]
			if  buscar_nom == res_nom:
				buscar_lista_desa.insert(x,x)
			x=x+1
		x=0
		while longitud2 > x:
			res_nom=lista_almuerzo[X]
			if buscar_nom == res_nom:
				buscar_lista_almu.insert(x,x)
			x=x+1
		x=0
		while longitud3 > x:
			res_nom=lista_cenas[x]
			if buscar_nom == res_nom:
				buscar_lista_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_desa)
		longitud2=len(buscar_lista_almu)
		longitud3=len(buscar_lista_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_nom=buscar_lista_desa[x]
			print "Nombre Desayuno", lista_desayunos[res_nom]
			print "Precio: ", lista_pre_desayunos[res_nom]
			print "Ingredientres: ", lista_ingre_desayunos[res_nom]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		while longitud2>x:
			res_nom=buscar_lista_almu[x]
			print "Nombre Desayuno", lista_almuerzo[res_nom]
			print "Precio: ", lista_pre_almuerzos[res_nom]
			print "Ingredientres: ", lista_ingre_almuerzos[res_nom]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		while longitud3>x:
			res_nom=buscar_lista_cena[x]
			print "Nombre Desayuno", lista_cenas[res_nom]
			print "Precio: ", lista_pre_cenas[res_nom]
			print "Ingredientres: ", lista_ingre_cenas[res_nom]
			nueva_line()
			x=x+1
	if opcion_dia==1 :
		longitud=len(desayuno_mexico)
		longitud2=len(almuerzo_mexico)
		longitud3=len(cena_mexico)
		x=0
		buscar_lista_desa=[]
		buscar_lista_almu=[]
		buscar_lista_cena=[]
		while longitud > x:
			res_nom=desayuno_mexico[x]
			if  buscar_nom == res_nom:
				buscar_lista_desa.insert(x,x)
			x=x+1
		x=0
		while longitud2 > x:
			res_nom=almuerzo_mexico[x]
			if buscar_nom == res_nom:
				buscar_lista_almu.insert(x,x)
			x=x+1
		x=0
		while longitud3 > x:
			res_nom=cena_mexico[x]
			if buscar_nom == res_nom:
				buscar_lista_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_desa)
		longitud2=len(buscar_lista_almu)
		longitud3=len(buscar_lista_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_nom=buscar_lista_desa[x]
			print "Nombre: ", desayuno_mexico[res_nom]
			print "Precio: ", precio_mexico_desa[res_nom]
			print "Ingredientres: ", ingre_mexico_desa[res_nom]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		while longitud2>x:
			res_nom=buscar_lista_almu[x]
			print "Nombre: ", almuerzo_mexico[res_nom]
			print "Precio: ", precio_mexico_almu[res_nom]
			print "Ingredientres: ", ingre_mexico_almu[res_nom]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		while longitud3>x:
			res_nom=buscar_lista_cena[x]
			print "Nombre: ", cena_mexico[res_nom]
			print "Precio: ", precio_mexico_cena[res_nom]
			print "Ingredientres: ", ingre_mexico_cena[res_nom]
			nueva_line()
			x=x+1
	if opcion_dia==3:
		longitud=len(desayuno_chile)
		longitud2=len(almuerzo_chile)
		longitud3=len(cena_chile)
		x=0
		buscar_lista_desa=[]
		buscar_lista_almu=[]
		buscar_lista_cena=[]
		while longitud > x:
			res_nom=desayuno_chile[x]
			if  buscar_nom == res_nom:
				buscar_lista_desa.insert(x,x)
			x=x+1
		x=0
		while longitud2 > x:
			res_nom=almuerzo_chile[x]
			if buscar_nom == res_nom:
				buscar_lista_almu.insert(x,x)
			x=x+1
		x=0
		while longitud3 > x:
			res_nom=cena_chile[x]
			if buscar_nom == res_nom:
				buscar_lista_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_desa)
		longitud2=len(buscar_lista_almu)
		longitud3=len(buscar_lista_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_nom=buscar_lista_desa[x]
			print "Nombre: ", desayuno_chile[res_nom]
			print "Precio: ", precio_chile_desa[res_nom]
			print "Ingredientres: ", ingre_chile_desa[res_nom]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		while longitud2>x:
			res_nom=buscar_lista_almu[x]
			print "Nombre: ", almuerzo_chile[res_nom]
			print "Precio: ", precio_chile_almu[res_nom]
			print "Ingredientres: ", ingre_chile_almu[res_nom]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		while longitud3>x:
			res_nom=buscar_lista_cena[x]
			print "Nombre: ", cena_chile[res_nom]
			print "Precio: ", precio_chile_cena[res_nom]
			print "Ingredientres: ", ingre_chile_cena[res_nom]
			nueva_line()
			x=x+1
	if opcion_dia==6:
		longitud=len(desayuno_peru)
		longitud2=len(almuerzo_peru)
		longitud3=len(cena_peru)
		x=0
		buscar_lista_desa=[]
		buscar_lista_almu=[]
		buscar_lista_cena=[]
		while longitud > x:
			res_nom=desayuno_peru[x]
			if  buscar_nom == res_nom:
				buscar_lista_desa.insert(x,x)
			x=x+1
		x=0
		while longitud2 > x:
			res_nom=almuerzo_peru[x]
			if buscar_nom == res_nom:
				buscar_lista_almu.insert(x,x)
			x=x+1
		x=0
		while longitud3 > x:
			res_nom=cena_peru[x]
			if buscar_nom == res_nom:
				buscar_lista_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_desa)
		longitud2=len(buscar_lista_almu)
		longitud3=len(buscar_lista_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_nom=buscar_lista_desa[x]
			print "Nombre: ", desayuno_peru[res_nom]
			print "Precio: ", precio_peru_desa[res_nom]
			print "Ingredientres: ", ingre_peru_desa[res_nom]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		while longitud2>x:
			res_nom=buscar_lista_almu[x]
			print "Nombre: ", almuerzo_peru[res_nom]
			print "Precio: ", precio_peru_almu[res_nom]
			print "Ingredientres: ", ingre_peru_almu[res_nom]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		while longitud3>x:
			res_nom=buscar_lista_cena[x]
			print "Nombre: ", cena_peru[res_nom]
			print "Precio: ", precio_peru_cena[res_nom]
			print "Ingredientres: ", ingre_peru_cena[res_nom]
			nueva_line()
			x=x+1
	menu_cliente()

#funcion para Bucar el mayo precio
def buscar_precio_mayor():
	print "Ingrese Precio mayor que"
	buscar_prec_mayor=input()
	if opcion_dia==2 or opcion_dia==4 or opcion_dia==5 or opcion_dia==7:
		longitud=len(lista_pre_desayunos)
		longitud2=len(lista_pre_almuerzos)
		longitud3=len(lista_pre_cenas)
		x=0
		buscar_lista_pre_desa=[]
		buscar_lista_pre_almu=[]
		buscar_lista_pre_cena=[]
		while longitud > x:
			res_pre=lista_pre_desayunos[x]
			if  buscar_prec_mayor<res_pre :
				buscar_lista_pre_desa.insert(x,x)
			x=x+1
		x=0
		while longitud2 > x:
			res_pre=lista_pre_almuerzo[X]
			if  buscar_prec_mayor<res_pre:
				buscar_lista_pre_almu.insert(x,x)
			x=x+1
		x=0
		while longitud3 > x:
			res_pre=lista_pre_cenas[x]
			if  buscar_prec_mayor<res_pre:
				buscar_lista_pre_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_pre_desa)
		longitud2=len(buscar_lista_pre_almu)
		longitud3=len(buscar_lista_pre_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_pre=buscar_lista_pre_desa[x]
			print "Nombre Desayuno", lista_desayunos[res_pre]
			print "Precio: ", lista_pre_desayunos[res_pre]
			print "Ingredientres: ", lista_ingre_desayunos[res_pre]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		x=0
		while longitud2>x:
			res_pre=buscar_lista_pre_almu[x]
			print "Nombre Desayuno", lista_almuerzo[res_pre]
			print "Precio: ", lista_pre_almuerzos[res_pre]
			print "Ingredientres: ", lista_ingre_almuerzos[res_pre]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		x=0
		while longitud3>x:
			res_pre=buscar_lista_pre_cena[x]
			print "Nombre Desayuno", lista_cenas[res_pre]
			print "Precio: ", lista_pre_cenas[res_pre]
			print "Ingredientres: ", lista_ingre_cenas[res_pre]
			nueva_line()
			x=x+1
	if opcion_dia==1 :
		longitud=len(precio_mexico_desa)
		longitud2=len(precio_mexico_almu)
		longitud3=len(precio_mexico_cena)
		x=0
		buscar_lista_desa=[]
		buscar_lista_almu=[]
		buscar_lista_cena=[]
		for x in range(longitud):
			res_pre=precio_mexico_desa[x]
			if  buscar_prec_mayor<res_pre:
				buscar_lista_desa.insert(x,x)
			x=x+1
		x=0
		for x in range(longitud2):
			res_pre=precio_mexico_almu[x]
			if  buscar_prec_mayor<res_pre :
				buscar_lista_almu.insert(x,x)
			x=x+1
		x=0
		for x in range(longitud3):
			res_pre=precio_mexico_cena[x]
			if  buscar_prec_mayor<res_pre :
				buscar_lista_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_desa)
		longitud2=len(buscar_lista_almu)
		longitud3=len(buscar_lista_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_pre=buscar_lista_desa[x]
			print "Nombre: ", desayuno_mexico[res_pre]
			print "Precio: ", precio_mexico_desa[res_pre]
			print "Ingredientres: ", ingre_mexico_desa[res_pre]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		x=0
		while longitud2>x:
			res_pre=buscar_lista_almu[x]
			print "Nombre: ", almuerzo_mexico[res_pre]
			print "Precio: ", precio_mexico_almu[res_pre]
			print "Ingredientres: ", ingre_mexico_almu[res_pre]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		x=0
		while longitud3>x:
			res_pre=buscar_lista_cena[x]
			print "Nombre: ", cena_mexico[res_pre]
			print "Precio: ", precio_mexico_cena[res_pre]
			print "Ingredientres: ", ingre_mexico_cena[res_pre]
			nueva_line()
			x=x+1
	if opcion_dia==3:
		longitud=len(precio_chile_desa)
		longitud2=len(precio_chile_almu)
		longitud3=len(precio_chile_cena)
		x=0
		buscar_lista_desa=[]
		buscar_lista_almu=[]
		buscar_lista_cena=[]
		while longitud > x:
			res_pre=precio_chile_desa[x]
			if  buscar_prec_mayor<res_pre:
				buscar_lista_desa.insert(x,x)
			x=x+1
		x=0
		while longitud2 > x:
			res_pre=precio_chile_almu[x]
			if  buscar_prec_mayor<res_pre :
				buscar_lista_almu.insert(x,x)
			x=x+1
		x=0
		while longitud3 > x:
			res_pre=precio_chile_cena[x]
			if  buscar_prec_mayor<res_pre :
				buscar_lista_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_desa)
		longitud2=len(buscar_lista_almu)
		longitud3=len(buscar_lista_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_pre=buscar_lista_desa[x]
			print "Nombre: ", desayuno_chile[res_pre]
			print "Precio: ", precio_chile_desa[res_pre]
			print "Ingredientres: ", ingre_chile_desa[res_pre]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		x=0
		while longitud2>x:
			res_pre=buscar_lista_almu[x]
			print "Nombre: ", almuerzo_chile[res_pre]
			print "Precio: ", precio_chile_almu[res_pre]
			print "Ingredientres: ", ingre_chile_almu[res_pre]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		x=0
		while longitud3>x:
			res_pre=buscar_lista_cena[x]
			print "Nombre: ", cena_chile[res_pre]
			print "Precio: ", precio_chile_cena[res_pre]
			print "Ingredientres: ", ingre_chile_cena[res_pre]
			nueva_line()
			x=x+1
	if opcion_dia==6:
		longitud=len(precio_peru_desa)
		longitud2=len(precio_peru_almu)
		longitud3=len(precio_peru_cena)
		x=0
		buscar_lista_desa=[]
		buscar_lista_almu=[]
		buscar_lista_cena=[]
		while longitud > x:
			res_pre=precio_peru_desa[x]
			if  buscar_prec_mayor<res_pre:
				buscar_lista_desa.insert(x,x)
			x=x+1
		x=0
		while longitud2 > x:
			res_pre=precio_peru_almu[x]
			if  buscar_prec_mayor<res_pre :
				buscar_lista_almu.insert(x,x)
			x=x+1
		x=0
		while longitud3 > x:
			res_pre=precio_peru_cena[x]
			if  buscar_prec_mayor<res_pre :
				buscar_lista_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_desa)
		longitud2=len(buscar_lista_almu)
		longitud3=len(buscar_lista_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_pre=buscar_lista_desa[x]
			print "Nombre: ", desayuno_peru[res_pre]
			print "Precio: ", precio_peru_desa[res_pre]
			print "Ingredientres: ", ingre_peru_desa[res_pre]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		x=0
		while longitud2>x:
			res_pre=buscar_lista_almu[x]
			print "Nombre: ", almuerzo_peru[res_pre]
			print "Precio: ", precio_peru_almu[res_pre]
			print "Ingredientres: ", ingre_peru_almu[res_pre]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		x=0
		while longitud3>x:
			res_pre=buscar_lista_cena[x]
			print "Nombre: ", cena_peru[res_pre]
			print "Precio: ", precio_peru_cena[res_pre]
			print "Ingredientres: ", ingre_peru_cena[res_pre]
			nueva_line()
			x=x+1
	menu_cliente()
	
#funcion para buscar el menor precio
def buscar_precio_menor():
	print "Ingrese Precio menor que"
	buscar_prec_menor=input()
	if opcion_dia==2 or opcion_dia==4 or opcion_dia==5 or opcion_dia==7:
		longitud=len(lista_pre_desayunos)
		longitud2=len(lista_pre_almuerzos)
		longitud3=len(lista_pre_cenas)
		x=0
		buscar_lista_pre_desa=[]
		buscar_lista_pre_almu=[]
		buscar_lista_pre_cena=[]
		while longitud > x:
			res_pre=lista_pre_desayunos[x]
			if  res_pre<buscar_prec_menor :
				buscar_lista_pre_desa.insert(x,x)
			x=x+1
		x=0
		while longitud2 > x:
			res_pre=lista_pre_almuerzo[X]
			if  res_pre<buscar_prec_menor :
				buscar_lista_pre_almu.insert(x,x)
			x=x+1
		x=0
		while longitud3 > x:
			res_pre=lista_pre_cenas[x]
			if  res_pre<buscar_prec_menor :
				buscar_lista_pre_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_pre_desa)
		longitud2=len(buscar_lista_pre_almu)
		longitud3=len(buscar_lista_pre_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_pre=buscar_lista_pre_desa[x]
			print "Nombre Desayuno", lista_desayunos[res_pre]
			print "Precio: ", lista_pre_desayunos[res_pre]
			print "Ingredientres: ", lista_ingre_desayunos[res_pre]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		x=0
		while longitud2>x:
			res_pre=buscar_lista_pre_almu[x]
			print "Nombre Desayuno", lista_almuerzo[res_pre]
			print "Precio: ", lista_pre_almuerzos[res_pre]
			print "Ingredientres: ", lista_ingre_almuerzos[res_pre]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		x=0
		while longitud3>x:
			res_pre=buscar_lista_pre_cena[x]
			print "Nombre Desayuno", lista_cenas[res_pre]
			print "Precio: ", lista_pre_cenas[res_pre]
			print "Ingredientres: ", lista_ingre_cenas[res_pre]
			nueva_line()
			x=x+1
	if opcion_dia==1 :
		longitud=len(precio_mexico_desa)
		longitud2=len(precio_mexico_almu)
		longitud3=len(precio_mexico_cena)
		x=0
		buscar_lista_desa=[]
		buscar_lista_almu=[]
		buscar_lista_cena=[]
		while longitud > x:
			res_pre=precio_mexico_desa[x]
			if  res_pre<buscar_prec_menor:
				buscar_lista_desa.insert(x,x)
			x=x+1
		x=0
		while longitud2 > x:
			res_pre=precio_mexico_almu[x]
			if  res_pre<buscar_prec_menor:
				buscar_lista_almu.insert(x,x)
			x=x+1
		x=0
		while longitud3 > x:
			res_pre=precio_mexico_cena[x]
			if  res_pre<buscar_prec_menor :
				buscar_lista_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_desa)
		longitud2=len(buscar_lista_almu)
		longitud3=len(buscar_lista_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_pre=buscar_lista_desa[x]
			print "Nombre: ", desayuno_mexico[res_pre]
			print "Precio: ", precio_mexico_desa[res_pre]
			print "Ingredientres: ", ingre_mexico_desa[res_pre]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		x=0
		while longitud2>x:
			res_pre=buscar_lista_almu[x]
			print "Nombre: ", almuerzo_mexico[res_pre]
			print "Precio: ", precio_mexico_almu[res_pre]
			print "Ingredientres: ", ingre_mexico_almu[res_pre]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		x=0
		while longitud3>x:
			res_pre=buscar_lista_cena[x]
			print "Nombre: ", cena_mexico[res_pre]
			print "Precio: ", precio_mexico_cena[res_pre]
			print "Ingredientres: ", ingre_mexico_cena[res_pre]
			nueva_line()
			x=x+1
	if opcion_dia==3:
		longitud=len(precio_chile_desa)
		longitud2=len(precio_chile_almu)
		longitud3=len(precio_chile_cena)
		x=0
		buscar_lista_desa=[]
		buscar_lista_almu=[]
		buscar_lista_cena=[]
		while longitud > x:
			res_pre=precio_chile_desa[x]
			if  res_pre<buscar_prec_menor :
				buscar_lista_desa.insert(x,x)
			x=x+1
		x=0
		while longitud2 > x:
			res_pre=precio_chile_almu[x]
			if  buscar_prec_menor<res_pre :
				buscar_lista_almu.insert(x,x)
			x=x+1
		x=0
		while longitud3 > x:
			res_pre=precio_chile_cena[x]
			if  res_pre<buscar_prec_menor :
				buscar_lista_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_desa)
		longitud2=len(buscar_lista_almu)
		longitud3=len(buscar_lista_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_pre=buscar_lista_desa[x]
			print "Nombre: ", desayuno_chile[res_pre]
			print "Precio: ", precio_chile_desa[res_pre]
			print "Ingredientres: ", ingre_chile_desa[res_pre]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		x=0
		while longitud2>x:
			res_pre=buscar_lista_almu[x]
			print "Nombre: ", almuerzo_chile[res_pre]
			print "Precio: ", precio_chile_almu[res_pre]
			print "Ingredientres: ", ingre_chile_almu[res_pre]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		x=0
		while longitud3>x:
			res_pre=buscar_lista_cena[x]
			print "Nombre: ", cena_chile[res_pre]
			print "Precio: ", precio_chile_cena[res_pre]
			print "Ingredientres: ", ingre_chile_cena[res_pre]
			nueva_line()
			x=x+1
	if opcion_dia==6:
		longitud=len(precio_peru_desa)
		longitud2=len(precio_peru_almu)
		longitud3=len(precio_peru_cena)
		x=0
		buscar_lista_desa=[]
		buscar_lista_almu=[]
		buscar_lista_cena=[]
		while longitud > x:
			res_pre=precio_peru_desa[x]
			if  res_pre<buscar_prec_menor :
				buscar_lista_desa.insert(x,x)
			x=x+1
		x=0
		while longitud2 > x:
			res_pre=precio_peru_almu[x]
			if  res_pre<buscar_prec_menor :
				buscar_lista_almu.insert(x,x)
			x=x+1
		x=0
		while longitud3 > x:
			res_pre=precio_peru_cena[x]
			if  res_pre<buscar_prec_menor :
				buscar_lista_cena.insert(x,x)
			x=x+1
		longitud=len(buscar_lista_desa)
		longitud2=len(buscar_lista_almu)
		longitud3=len(buscar_lista_cena)
		x=0
		if longitud>=0:
			print "------Desayunos----"
		while longitud>x:
			res_pre=buscar_lista_desa[x]
			print "Nombre: ", desayuno_peru[res_pre]
			print "Precio: ", precio_peru_desa[res_pre]
			print "Ingredientres: ", ingre_peru_desa[res_pre]
			nueva_line()
			x=x+1
		if longitud2>=0:
			print "------Almuerzos------"
		x=0
		while longitud2>x:
			res_pre=buscar_lista_almu[x]
			print "Nombre: ", almuerzo_peru[res_pre]
			print "Precio: ", precio_peru_almu[res_pre]
			print "Ingredientres: ", ingre_peru_almu[res_pre]
			nueva_line()
			x=x+1
		if longitud3>=0:
			print "-----Cenas-----"
		x=0
		while longitud3>x:
			res_pre=buscar_lista_cena[x]
			print "Nombre: ", cena_peru[res_pre]
			print "Precio: ", precio_peru_cena[res_pre]
			print "Ingredientres: ", ingre_peru_cena[res_pre]
			nueva_line()
			x=x+1
	menu_cliente()
Inicio()

