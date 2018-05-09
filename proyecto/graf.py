#! /usr/bin/env python
# Proyecto.

from tkinter import *
from tkinter import ttk

def Register():
    f=open('./registro2.txt','a')
    registroNuevo = ""
    for key, value in registro.items():
        registroNuevo += value.get() + ", "
    f.write(registroNuevo + '\n')
    f.close()

def afunc():
    Label(registerFrame, text="Nombre").place(x=10, y=10)
    registro['nombre'] = StringVar()
    Entry(registerFrame, textvariable=registro['nombre']).place(x=10,y=30)

    Label(registerFrame, text="Apellido Paterno").place(x=160, y=10)
    registro['apellido1'] = StringVar()
    Entry(registerFrame, textvariable=registro['apellido1']).place(x=160,y=30)

    Label(registerFrame, text="Apellido Paterno").place(x=310, y=10)
    registro['apellido2'] = StringVar()
    Entry(registerFrame, textvariable=registro['apellido2']).place(x=310,y=30)

    Label(registerFrame, text="Cargo").place(x=460, y=10)
    registro['cargo'] = StringVar()
    Entry(registerFrame, textvariable=registro['cargo']).place(x=460,y=30)

    Label(registerFrame, text="Empresa").place(x=610, y=10)
    registro['empresa'] = StringVar()
    Entry(registerFrame, textvariable=registro['empresa']).place(x=610,y=30)

    Label(registerFrame, text="Calle").place(x=10, y=80)
    registro['calle'] = StringVar()
    Entry(registerFrame, textvariable=registro['calle']).place(x=10,y=100)

    Label(registerFrame, text="Numero Exterior").place(x=160, y=80)
    registro['numeroExt'] = StringVar()
    Entry(registerFrame, textvariable=registro['numeroExt']).place(x=160,y=100)

    Label(registerFrame, text="Numero Interior").place(x=310, y=80)
    registro['numeroInt'] = StringVar()
    Entry(registerFrame, textvariable=registro['numeroInt']).place(x=310,y=100)

    Label(registerFrame, text="Colonia").place(x=460, y=80)
    registro['colonia'] = StringVar()
    Entry(registerFrame, textvariable=registro['colonia']).place(x=460,y=100)

    Label(registerFrame, text="Municipio").place(x=610, y=80)
    registro['municipio'] = StringVar()
    Entry(registerFrame, textvariable=registro['municipio']).place(x=610,y=100)

    Label(registerFrame, text="Estado").place(x=10, y=130)
    registro['estado'] = StringVar()
    Entry(registerFrame, textvariable=registro['estado']).place(x=10,y=150 )

    Label(registerFrame, text="Codigo Postal").place(x=160, y=130)
    registro['codigoPostal'] = StringVar()
    Entry(registerFrame, textvariable=registro['codigoPostal']).place(x=160,y=150)

    Label(registerFrame, text="Telefono").place(x=310, y=130)
    registro['telefono'] = StringVar()
    Entry(registerFrame, textvariable=registro['telefono']).place(x=310,y=150)

    Label(registerFrame, text="Correo Electronico").place(x=460, y=130)
    registro['correoElectronico'] = StringVar()
    Entry(registerFrame, textvariable=registro['correoElectronico']).place(x=460,y=150)

    Label(registerFrame, text="Fecha de Nacimieto").place(x=610, y=130)
    registro['fechaNacimiento'] = StringVar()
    Entry(registerFrame, textvariable=registro['fechaNacimiento']).place(x=610,y=150)

    Button(registerFrame, command=Register, text="Agregar").place(x=350,y=180)

registro = dict.fromkeys(['nombre', 'apellido1', 'apellido2', 'cargo', 'empresa', 'calle',
 'numeroExt', 'numeroInt', 'colonia','municipio', 'estado', 'codigoPostal',
 'telefono', 'correoElectronico', 'fechaNacimiento'])

root = Tk()
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand="yes")

registerFrame = ttk.Frame()
listRegistersFrame = ttk.Frame()

notebook.add(registerFrame, text="Registrar")
notebook.add(listRegistersFrame, text="Listado de Registros")

afunc()

# createRegisterWindow()


root.geometry("800x800")
root.mainloop()

# createMainFrame()
