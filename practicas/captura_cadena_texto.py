#! /usr/bin/env python
# Practica 2.
# Autor: Luis David Gutiérrez Peña

def isFirstMayus(cadena = ''):
    return cadena[0].isupper()

def wordLen(cadena = ''):
    return len(cadena.split(' '))

def splitByWords(cadena = ''):
    return cadena.split(' ')

def stringReverse(cadena = ''):
    return cadena[::-1]

# def stringReverse(cadena = ''):
#     return cadena.split(' ').reverse()

def upperLastLetterInWords(cadena = ''):
    cadena = cadena.split(' ')
    for index, palabra in enumerate(cadena):
        cadena[index] = cadena[index].replace(cadena[index][-1], cadena[index][-1].upper())
    return cadena

cadena = raw_input("Ingrese cualquier cadena de texto: ")
if isFirstMayus(cadena):
    print("Es mayuscula")
else:
    print("No es mayuscula")
print("Numero de palabras: " + str(wordLen(cadena)))
print("Lista de palabras", splitByWords(cadena))
print("Cadena inverida",stringReverse(cadena))
print("Ultima letra de cada palabra en mayuscula", upperLastLetterInWords(cadena))
