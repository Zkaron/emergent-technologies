#! /usr/bin/env python
# Practica 1. 
# Autor: Luis David Gutiérrez Peña

def imprimeLista(lista = []):
    arrayNumeros = []
    for i in range(len(lista)):
        arrayNumeros.append(lista[i])
    print(arrayNumeros)

def sliceHalfList(lista = []):
    print('Substring de dos elementos desde la mitad de la lista')
    half = len(lista) / 2
    return lista[half:half+2]

def listCube(lista = []):
    print('Elementos lista elevados al cubo')
    return list(map(cubo, lista))
    # for i in range(len(lista)):
    #     lista[i] = pow(lista[i], 3)
    # return lista

def cubo(x):
    return x*x*x

# def orderAsc(lista = []):
#     lista.sort()
#     return lista

# Main
listaNumeros = []
while 1:
    numero = input("Ingrese un numero [escriba -1 para terminar]: ")
    if numero == -1:
        break;
    listaNumeros.append(numero)

print('Lista original')
imprimeLista(listaNumeros)
mitadLista = sliceHalfList(listaNumeros)
imprimeLista(mitadLista)
print('Primer y utlimo elemento de la lista')
print("[" + str(listaNumeros[0]) + ', ' + str(listaNumeros[-1]) + "]")
listaNumeros = sorted(listaNumeros)
print('Lista ordenada menor a mayor')
imprimeLista(listaNumeros)
listaNumeros = sorted(listaNumeros, reverse=True)
print('Lista ordenada mayor a menor')
imprimeLista(listaNumeros)
listaNumeros = listCube(listaNumeros);
imprimeLista(listaNumeros)
