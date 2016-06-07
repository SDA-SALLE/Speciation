# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import os
import sys
import json
sys.path.append('core')
from excelmatriz import *
from clear import *

def listaCSV(direccion):
   	#Variable para la ruta al directorio
	path = os.path.join(direccion,'')
	#print direccion

	#Lista vacia para incluir los ficheros
	lstFilesEmissions = []

	#Lista con todos los ficheros del directorio:
	lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
	datos = {}

	#Crea una lista de los ficheros que existen en el directorio y los incluye a la lista.
	for root, dirs, files in lstDir:
	    for fichero in files:
	        (nombreFichero, extension) = os.path.splitext(fichero)
	        if(extension == '.csv'):
	        	lstFilesEmissions.append(nombreFichero+extension)

	return lstFilesEmissions



def unions(identy):
	if identy == 'VP':
		listHabilPrincipal = []
		listNHabilPrincipal = []

		listHabilSecundary = []
		listNHabilSecundary = []

		listHabilTM = []
		listNHabilTM = []

		folder = os.path.join('..', 'data', 'in', 'unions', '')
		listout = listaCSV(folder)
		#print listout
		
		for out in listout:

			if 'Principal' in out:
				if 'ENH' in out or 'NHABIL' in out or '_NHabil' in out:
					listNHabilPrincipal.append(out)
				elif 'EH' in out or 'HABIL' in out or '_Habil' in out:
					listHabilPrincipal.append(out)

			elif 'Secundary' in out:
				if 'ENH' in out or 'NHABIL' in out or '_NHabil' in out:
					listNHabilSecundary.append(out)
				elif 'EH' in out or 'HABIL' in out or '_Habil' in out:
					listHabilSecundary.append(out)

			elif 'TM' in out:
				if 'ENH' in out or 'NHABIL' in out or '_NHabil' in out:
					listNHabilTM.append(out)
				elif 'EH' in out or 'HABIL' in out or '_Habil' in out:
					listHabilTM.append(out)

		listHabil = [listHabilPrincipal, listHabilTM, listHabilSecundary]
		listNHabil = [listNHabilPrincipal, listNHabilTM, listNHabilSecundary]
		

		foldersave = os.path.join('..', 'data', 'out', 'unions', '')
		for lista in listNHabil:

			if 'Principal' in lista[0]:
				csvsalida = open(foldersave + 'Principal_' + 'NHabil_Full.csv', 'w')
			if 'TM' in lista[0]:
				csvsalida = open(foldersave + 'TM_' + 'NHabil_Full.csv', 'w')
			if 'Secundary' in lista[0]:
				csvsalida = open(foldersave + 'Secundary_' + 'NHabil_Full.csv', 'w')

			salida = csv.writer(csvsalida, delimiter=',')
			salida.writerow(['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h'])

			archive = folder + archiv
			matriz = convertCSVMatriz (archive)
			for i in range(1, matriz.shape[0]):
				for x in range(0, matriz.shape[1]):
					if x == 0:
						csvsalida.write(matriz[i][x])
					else:
						csvsalida.write(',')
						csvsalida.write(matriz[i][x])
				csvsalida.write('\n')

			matriz = None

		for lista in listHabil:
			if 'Principal' in lista[0]:
				csvsalida = open(foldersave + 'Principal_' + 'Habil_Full.csv', 'w')
			if 'TM' in lista[0]:
				csvsalida = open(foldersave + 'TM_' + 'Habil_Full.csv', 'w')
			if 'Secundary' in lista[0]:
				csvsalida = open(foldersave + 'Secundary_' + 'Habil_Full.csv', 'w')

			salida = csv.writer(csvsalida, delimiter=',')
			salida.writerow(['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h'])
			
			archive = folder + archiv
			matriz = convertCSVMatriz (archive)
			for i in range(1, matriz.shape[0]):
				for x in range(0, matriz.shape[1]):
					if x == 0:
						csvsalida.write(matriz[i][x])
					else:
						csvsalida.write(',')
						csvsalida.write(matriz[i][x])
				csvsalida.write('\n')
				#salida.writerow(matriz[i,:])

			matriz = None

	elif identy == 'VNP':
		folder = os.path.join('..', 'data', 'in', 'unions', '')
		foldersave = os.path.join('..', 'data', 'out', 'unions', '')
		listout = listaCSV(folder)
		listIndustrial = []
		listPublic = []
		#print listout
		for out in listout:
			if 'Industrial' in out:
				listIndustrial.append(out)
			if 'Public' in out or 'Publi' in out:
				listPublic.append(out)
		#print listIndustrial

		csvsalida = open(foldersave + 'Industrial_' + 'Full.csv', 'w')
		salida = csv.writer(csvsalida, delimiter=',')
		salida.writerow(['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h'])
		for lista in listIndustrial:
			archive = folder + lista
			print archive
			matriz = convertCSVMatriz (archive)
			for i in range(1, matriz.shape[0]):
				for x in range(0, matriz.shape[1]):
					if x == 0:
						csvsalida.write(matriz[i][x])
					else:
						csvsalida.write(',')
						csvsalida.write(matriz[i][x])
				csvsalida.write('\n')
				#salida.writerow(matriz[i,:])

		csvsalida = open(foldersave + 'Public_' + 'Full.csv', 'w')
		salida = csv.writer(csvsalida, delimiter=',')
		salida.writerow(['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h'])
		for lista in listPublic:
			archive = folder + lista
			matriz = convertCSVMatriz (archive)
			for i in range(1, matriz.shape[0]):
				for x in range(0, matriz.shape[1]):
					if x == 0:
						csvsalida.write(matriz[i][x])
					else:
						csvsalida.write(',')
						csvsalida.write(matriz[i][x])
				csvsalida.write('\n')
				#salida.writerow(matriz[i,:])

	elif identy == 'moviles':
		listHabil = []
		listNHabil = []

		folder = os.path.join('..', 'data', 'in', 'unions', '')
		listout = listaCSV(folder)
		
		for out in listout:

			if 'ENH' in out or 'NHABIL' in out or '_NHabil' in out:
				listNHabil.append(out)
			elif 'EH' in out or 'HABIL' in out or '_Habil' in out:
				listHabil.append(out)

		foldersave = os.path.join('..', 'data', 'out', 'unions', '')
		
		csvsalida = open(foldersave + 'NHabil_Full.csv', 'w')
		names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
		for name in names:
			if name == 'ROW':
				csvsalida.write(name)
			else:
				csvsalida.write(',')
				csvsalida.write(name)
		csvsalida.write('\n')
		for lista in listNHabil:
			archive = folder + lista
			matriz = convertCSVMatriz (archive)
			for i in range(1, matriz.shape[0]):
				for x in range(0, matriz.shape[1]):
					if x == 0:
						csvsalida.write(matriz[i][x])
					else:
						csvsalida.write(',')
						csvsalida.write(matriz[i][x])
				csvsalida.write('\n')
			matriz = None
		csvsalida.close()

		csvsalida = open(foldersave + 'Habil_Full.csv', 'w')
		for name in names:
			if name == 'ROW':
				csvsalida.write(name)
			else:
				csvsalida.write(',')
				csvsalida.write(name)
		csvsalida.write('\n')
		for lista in listHabil:
			archive = folder + lista
			matriz = convertCSVMatriz (archive)
			for i in range(1, matriz.shape[0]):
				for x in range(0, matriz.shape[1]):
					if x == 0:
						csvsalida.write(matriz[i][x])
					else:
						csvsalida.write(',')
						csvsalida.write(matriz[i][x])
				csvsalida.write('\n')
				#salida.writerow(matriz[i,:])

			matriz = None
		csvsalida.close()
		
def final(Archive):
	
	data = {}
	matriz = convertCSVMatriz(Archive)
	head = matriz[0,:]
	index = 0
	
	for value in head:
		if value == 'ROW':
			colROW = index
		if value == 'COL':
			colCOL = index
		if value == 'LAT':
			colLAT = index
		if value == 'LON':
			colLON = index
		if value == 'POLNAME':
			colPollname = index
		if value == 'UNIT':
			colUnit = index
		index += 1


	for i in range(1, matriz.shape[0]):
		keys = matriz[i][colROW] + matriz[i][colCOL] + matriz[i][colPollname]
		
		if data.get(keys) is None:
			data[keys] = {}
			data[keys]['hours'] = {}
			data[keys]['GENERAL'] = {'ROW': [], 'COL': [], 'LAT': [], 'LON': [], 'POLNAME': [], 'UNIT':[]}

		
		for hour in range(0, 25):
			data[keys]['hours'][hour] = []

	
	for i in range(1, matriz.shape[0]):
		keys = matriz[i][colROW] + matriz[i][colCOL] + matriz[i][colPollname]
		if data[keys]['GENERAL']['ROW'] == []:
			data[keys]['GENERAL']['ROW'].append(matriz[i][colROW])
			data[keys]['GENERAL']['COL'].append(matriz[i][colCOL])
			data[keys]['GENERAL']['LAT'].append(matriz[i][colLAT])
			data[keys]['GENERAL']['LON'].append(matriz[i][colLON])
			data[keys]['GENERAL']['POLNAME'].append(matriz[i][colPollname])
			data[keys]['GENERAL']['UNIT'].append(matriz[i][colUnit])

		hour = 0
		for x in range(6, matriz.shape[1]):
			data[keys]['hours'][hour].append(matriz[i][x])
			hour += 1

	matriz = None
	keys = data.keys()
	for key in keys:
		hours = data[key]['hours'].keys()
		for hour in hours:
			if hour == 'GENERAL':
				pass
			else:
				suma = eval('+'.join(data[key]['hours'][hour]))
				data[key]['hours'][hour] = []
				data[key]['hours'][hour].append(suma)

	
	csvsalida = open(Archive, 'w')
	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names:
		if name == 'ROW':
			csvsalida.write(name)
		else:
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	names = data.keys()

	for key in names:
		csvsalida.write(data[key]['GENERAL']['ROW'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['COL'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['LAT'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['LON'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['POLNAME'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['UNIT'][0])
		#csvsalida.write(',')
		hours = data[key]['hours'].keys()
		for hour in hours:
			csvsalida.write(',')
			csvsalida.write(str(data[key]['hours'][hour][0]))
		csvsalida.write('\n')
	csvsalida.close ()



folder = os.path.join('..', 'data', 'out', 'unions', '')
clear(folder)

print 'Write archives unions'
print 'If Mobiles write, MOB'


user = raw_input('Insert option: ')
#unions('VP')
#total('VP')

unions('moviles')

folder = os.path.join('..', 'data', 'out', 'unions', '')
lista = listaCSV(folder)
for archiv in lista:
	archive = folder + archiv
	final(archive)




