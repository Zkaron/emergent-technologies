#! /usr/bin/env python
# Practica 3.

import time
from datetime import datetime, date

def openFile(path, type):
    try:
        f = open(path, type)
        # print("Archivo", path, 'abierto!')
        return f
    except Exception as e:
        print(e)
        exit()


datos = ['nombre', 'apellido1', 'apellido2', 'cargo', 'empresa', 'calle',
 'numeroExt', 'numeroInt', 'colonia','municipio', 'estado', 'codigoPostal',
 'telefono', 'correoElectronico', 'fechaNacimiento', 'edadCalculada']
today = date.today()

# Get registers from file and save it into a dictionary
registros = []
f = openFile('./registros.txt', 'r')
for linea in f:
    linea = linea[:-1]
    registro = dict([(key, value) for key, value in zip(datos, linea.split(','))])
    registro['edadCalculada'] = str(int(abs(today - datetime.strptime(registro['fechaNacimiento'], '%d/%m/%Y').date()).days / 365.25))

    registros.append(registro)

# print(registros[0]['nombre'])

#Leer oficio-template
f = openFile('./oficio-template.txt', 'r')
oficioTemplate = f.read()
for registro in registros:
    registroTemplate = oficioTemplate
    # print('itera', registro['nombre'])
    while registroTemplate.find('[') != -1:
        inicio = registroTemplate.find('[')
        if inicio != -1:
            fin = registroTemplate.find(']')
            reemplazar = registroTemplate[inicio:fin+1]
            propiedad = str(registroTemplate[inicio+1:fin])
            registroTemplate = registroTemplate.replace(reemplazar, registro[propiedad])
    oficio = openFile('./oficios-generados/' + registro['nombre'] + '-oficio.txt', 'w+')
    oficio.write(registroTemplate)

    # shutil.move('./' + registro['nombre'] + '-oficio.txt', './oficios-generados/' + registro['nombre'] + '-oficio.txt')

# print(oficioTemplate)
