#! /usr/bin/env python
# Practica 3.

def validaCorreo(correo = ''):
    arroba = correo.find('@')
    nombre = correo[0:arroba]
    indiceSubdominio = correo.find('.', arroba)
    # indiceSubdominio = correo.rfind('.') #tambien funciona
    dominio = correo[arroba:indiceSubdominio]
    subdominio = correo[indiceSubdominio: -1]

    if arroba != -1 and nombre != '' and indiceSubdominio != -1 and dominio != '' and subdominio != '':
        return True
    return False


correo = raw_input('Ingrese un correo: ')
if(validaCorreo(correo)):
    print("Correo es valido")
else:
    print("Correo no es valido")
