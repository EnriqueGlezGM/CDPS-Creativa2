#!/usr/bin/python
#coding=utf-8


#PRACTICA CREATIVA PARA EL EXAMEN FINAL

# Alumnos:
# Enrique Gonzalez Macias
# Roberto Martin Luengo


#######################################################################################
######		   		 Configuración del FW			         ######
#######################################################################################
###### 			      1. Copia del archivo fw.fw 		         ######
######   		  	  2. Configuración		 		 ###### 
#######################################################################################


from subprocess import call


def funcion_fw(comando, copy = False):
	if (copy == False) :
		cmd_line = "sudo lxc-attach --clear-env -n fw -- "+comando;
		call(cmd_line, shell=True);
	else:
		print("\033[0;34m"+"\n"+comando+"\033[0;m");
		cmd_line = "sudo /lab/cdps/bin/cp2lxc fw.fw /var/lib/lxc/fw/rootfs/root";
		call(cmd_line, shell=True);

#######################################################################################################################
################################# 	   1. Copia del archivo fw.fw 	        #######################################
#######################################################################################################################

print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");

print("\033[1;30m"+"Iniciando Configuración del FW...\n"+"\033[0;m");


funcion_fw("Copiando fw.fw al firewall", True);

# http://fwbuilder.sourceforge.net/4.0/docs/users_guide5/UsersGuide5.pdf

#######################################################################################################################
##################################### 	       2. Configuración 	    ###########################################
#######################################################################################################################


funcion_fw("chmod 777 /root/fw.fw"); 

funcion_fw("/root/fw.fw");

print("\033[1;32m"+"\nLa configuración se ha realizado con exito"+"\033[0;m");


print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");




