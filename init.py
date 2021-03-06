#!/usr/bin/python
#coding=utf-8


#PRACTICA CREATIVA PARA EL EXAMEN FINAL

# Alumnos:
# Enrique Gonzalez Macias
# Roberto Martin Luengo

#######################################################################################
######		   	Instalación y arranque del entorno			 ######
#######################################################################################
###### 				  1. Instalacion		          	 ######
######   		   	   2. Arranque		     			 ###### 
#######################################################################################

from subprocess import call	
import os

def funcion_init(comando):
	cmd_line = comando;
	call(cmd_line, shell=True);

#######################################################################################################################
#######################################     		1. Instalacion 		#######################################
#######################################################################################################################

print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");

print("\033[1;30m"+"Instalando escenario...\n"+"\033[0;m");


os.chdir("/mnt/tmp")

funcion_init("wget http://idefix.dit.upm.es/cdps/pc2/pc2.tgz")

funcion_init("sudo vnx --unpack pc2.tgz")

os.chdir("/mnt/tmp/scripts")

funcion_init("chmod 777 s4.py");

funcion_init("python s4.py");

funcion_init("chmod 777 nagios-mv.py");

funcion_init("python nagios-mv.py");

funcion_init("chmod 777 bbdd2.py");

funcion_init("python bbdd2.py");

os.chdir("/mnt/tmp/pc2")

funcion_init("bin/prepare-pc2-labo")


print("\033[1;32m"+"\nEscenario instalado\n"+"\033[0;m");

print("\033[1;30m"+"\n---------------------------------------------------------------------------------------------------------\n"+"\033[0;m");

#######################################################################################################################
#######################################     		2. Arranque 		#######################################
#######################################################################################################################


print("\033[1;30m"+"Arrancando escenario...\n"+"\033[0;m");

funcion_init("sudo vnx -f pc2.xml --create")


print("\033[1;32m"+"\nEscenario arrancado\n"+"\033[0;m");



print("\033[1;30m"+"********************************************************************************************************\n"+"\033[0;m");

