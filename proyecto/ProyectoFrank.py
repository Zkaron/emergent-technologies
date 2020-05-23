#! /usr/bin/env python
# Proyecto.

from tkinter import *
from tkinter import ttk
import time
from datetime import datetime, date
import uuid

# Añade un nuevo registro a la Base de Datos (Final del Archivo)
def Register():
    registroNuevo['uuid'] = StringVar(uuid.uuid4())
    registroStr = ""
    for key, value in registroNuevo.items():
        if key != 'uuid':
            registroNuevo[key] = value.get()
        registroStr += registroNuevo[key] + ", "

    f=open('./registros.data','a')
    f.write(registroStr[0:-2] + '\n')  # Se omite la última coma y espacio
    f.close()

    # Inserta los nuevos datos en la lista (Actualizacion)
    registroNuevo['edadCalculada'] = str(int(abs(today - datetime.strptime(registroNuevo['fechaNacimiento'], '%d/%m/%Y').date()).days / 365.25))
    registros.append(registroNuevo)
    listboxRegister.append(registroNuevo['nombre'] + " " + registroNuevo['apellido1'] + " " + registroNuevo['apellido2'])
    registers.set(listboxRegister)

def Edit():

    edicionStr = ""
    for key,value in registroEdicion.items():
        if key != 'uuid':
            registros[itemSelected][key] = value.get()
        if key != 'edadCalculada':
            edicionStr += registros[itemSelected][key] + ", "

    uuid = registroEdicion['uuid']
    f = open('./registros.data', 'r+')
    db = f.readlines()
    f.seek(0)
    for line in db:
        if line.startswith(uuid) == False:
            f.write(line)
        else:
            f.write(edicionStr[:-2] + '\n')
    f.truncate()
    f.close()

    registros[itemSelected]['edadCalculada'] = str(int(abs(today - datetime.strptime(registros[itemSelected]['fechaNacimiento'], '%d/%m/%Y').date()).days / 365.25))
    listboxRegister[itemSelected] = (registros[itemSelected]['nombre'] + " " + registros[itemSelected]['apellido1'] + " " + registros[itemSelected]['apellido2'])
    registers.set(listboxRegister)
    deactivateEdition()

def Delete():
    uuid = registros[itemSelected]['uuid']

    f = open('./registros.data', 'r+')
    db = f.readlines()
    f.seek(0)
    for line in db:
        if line.find(uuid) == -1:
            f.write(line)
    f.truncate()
    f.close()

    registros.pop(itemSelected)
    listboxRegister.pop(itemSelected)
    registers.set(listboxRegister)

def showCurrentSelected(*args):
    global itemSelected
    index = listbox.curselection()
    if len(index) == 1:
        itemSelected = int(index[0])
        for key,value in registros[itemSelected].items():
            if key == 'uuid':
                registroEdicion[key] = value
            else:
                registroEdicion[key].set(value)

def getRegisters():
    # global currentId
    # currentId = 0
    regsData = open('./registros.data', 'r')
    for line in regsData:
        line = line[:-1]
        # currentId += 1
        registro = dict([(key, value) for key, value in zip(datos, line.split(', '))])
        registro['edadCalculada'] = str(int(abs(today - datetime.strptime(registro['fechaNacimiento'], '%d/%m/%Y').date()).days / 365.25))

        registros.append(registro)
    regsData.close()

    # global listboxRegister
    # listboxRegister = []
    var = []
    for reg in registros:
        listboxRegister.append(reg['nombre'] + " " + reg['apellido1'] + " " + reg['apellido2'])

    registers.set(listboxRegister)

def activateEdition():
    for entry in editEntries:
        entry.config(state='normal')
    makeEditionBtn.config(state='normal')
    cancelEditionBtn.config(state='normal')
    listbox.config(state='disabled')

def deactivateEdition():
    for entry in editEntries:
        entry.config(state='disabled')
    makeEditionBtn.config(state='disabled')
    cancelEditionBtn.config(state='disabled')
    listbox.config(state='normal')

datos = ['uuid', 'nombre', 'apellido1', 'apellido2', 'cargo', 'empresa', 'calle',
 'numeroExt', 'numeroInt', 'colonia','municipio', 'estado', 'codigoPostal',
 'telefono', 'correoElectronico', 'fechaNacimiento']
registros = []
registroNuevo = dict.fromkeys(datos)
registroEdicion = dict.fromkeys(datos)
listboxRegister = []
itemSelected = -1

# Fecha actual
today = date.today()

#creacion "dinamica" de Entries (input)
registerEntries = []
editEntries = []

# Se crea ventana principal
root = Tk()
#aqui se almacena todo lo del listbox
registers = StringVar()

#Obtenemos informacion de la base de datos ya que existe 'registers'
getRegisters()
# Se crea frame de pestañas
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand="yes")

# Se crean los Frames que van dentro de las pestañas
registerFrame = ttk.Frame()
listRegistersFrame = ttk.Frame()

# Se añaden los Frames a las pestañas
notebook.add(registerFrame, text="Registrar")
notebook.add(listRegistersFrame, text="Listado de Registros")

#------------------CREACION DE VISTA DE REGISTRO---------------#
Label(registerFrame, text="Nombre").place(x=10, y=30)
registroNuevo['nombre'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['nombre']).place(x=10,y=50)

Label(registerFrame, text="Apellido Paterno").place(x=160, y=30)
registroNuevo['apellido1'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['apellido1']).place(x=160,y=50)

Label(registerFrame, text="Apellido Paterno").place(x=310, y=30)
registroNuevo['apellido2'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['apellido2']).place(x=310,y=50)

Label(registerFrame, text="Cargo").place(x=460, y=30)
registroNuevo['cargo'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['cargo']).place(x=460,y=50)

Label(registerFrame, text="Empresa").place(x=610, y=30)
registroNuevo['empresa'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['empresa']).place(x=610,y=50)

Label(registerFrame, text="Calle").place(x=10, y=80)
registroNuevo['calle'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['calle']).place(x=10,y=100)

Label(registerFrame, text="Numero Exterior").place(x=160, y=80)
registroNuevo['numeroExt'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['numeroExt']).place(x=160,y=100)

Label(registerFrame, text="Numero Interior").place(x=310, y=80)
registroNuevo['numeroInt'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['numeroInt']).place(x=310,y=100)

Label(registerFrame, text="Colonia").place(x=460, y=80)
registroNuevo['colonia'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['colonia']).place(x=460,y=100)

Label(registerFrame, text="Municipio").place(x=610, y=80)
registroNuevo['municipio'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['municipio']).place(x=610,y=100)

Label(registerFrame, text="Estado").place(x=10, y=130)
registroNuevo['estado'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['estado']).place(x=10,y=150 )

Label(registerFrame, text="Codigo Postal").place(x=160, y=130)
registroNuevo['codigoPostal'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['codigoPostal']).place(x=160,y=150)

Label(registerFrame, text="Telefono").place(x=310, y=130)
registroNuevo['telefono'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['telefono']).place(x=310,y=150)

Label(registerFrame, text="Correo Electronico").place(x=460, y=130)
registroNuevo['correoElectronico'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['correoElectronico']).place(x=460,y=150)

Label(registerFrame, text="Fecha de Nacimieto").place(x=610, y=130)
registroNuevo['fechaNacimiento'] = StringVar()
Entry(registerFrame, textvariable=registroNuevo['fechaNacimiento']).place(x=610,y=150)

Button(registerFrame, command=Register, text="Agregar").place(x=350,y=180)
#------------------FIN DE VISTA DE REGISTRO---------------#


#------------------CREACION DE VISTA DE LISTADO---------------#
#------------------LISTBOX------------------#
listbox = Listbox(listRegistersFrame, listvariable=registers, width="30", height="10")
s = ttk.Scrollbar(listRegistersFrame, orient=VERTICAL, command=listbox.yview)
listbox.configure(yscrollcommand=s.set)
listbox.place(x=50, y=30)

btnGenerate = Button(listRegistersFrame, command=activateEdition, text="Generar Oficio")
btnEdit = Button(listRegistersFrame, command=activateEdition, text="Modificar")
btnRemove = Button(listRegistersFrame, command=Delete, text="Dar de Baja")

btnGenerate.place(x=250, y=50)
btnEdit.place(x=250, y=100)
btnRemove.place(x=250, y=150)

listbox.bind('<<ListboxSelect>>', showCurrentSelected)
# listbox.bind('<Double-1>', activateEdition)
# listbox.bind('<Return>', activateEdition)

# ----------------- EDIT -------------------------#
Label(listRegistersFrame, text="Nombre").place(x=410, y=30)
registroEdicion['nombre'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['nombre']))

Label(listRegistersFrame, text="Apellido Paterno").place(x=560, y=30)
registroEdicion['apellido1'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['apellido1']))

Label(listRegistersFrame, text="Apellido Paterno").place(x=710, y=30)
registroEdicion['apellido2'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['apellido2']))

Label(listRegistersFrame, text="Cargo").place(x=860, y=30)
registroEdicion['cargo'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['cargo']))

Label(listRegistersFrame, text="Empresa").place(x=1010, y=30)
registroEdicion['empresa'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['empresa']))

Label(listRegistersFrame, text="Calle").place(x=410, y=80)
registroEdicion['calle'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['calle']))

Label(listRegistersFrame, text="Numero Exterior").place(x=560, y=80)
registroEdicion['numeroExt'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['numeroExt']))

Label(listRegistersFrame, text="Numero Interior").place(x=710, y=80)
registroEdicion['numeroInt'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['numeroInt']))

Label(listRegistersFrame, text="Colonia").place(x=860, y=80)
registroEdicion['colonia'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['colonia']))

Label(listRegistersFrame, text="Municipio").place(x=1010, y=80)
registroEdicion['municipio'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['municipio']))

Label(listRegistersFrame, text="Estado").place(x=410, y=130)
registroEdicion['estado'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['estado']))

Label(listRegistersFrame, text="Codigo Postal").place(x=560, y=130)
registroEdicion['codigoPostal'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['codigoPostal']))

Label(listRegistersFrame, text="Telefono").place(x=710, y=130)
registroEdicion['telefono'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['telefono']))

Label(listRegistersFrame, text="Correo Electronico").place(x=860, y=130)
registroEdicion['correoElectronico'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['correoElectronico']))

Label(listRegistersFrame, text="Fecha de Nacimieto").place(x=1010, y=130)
registroEdicion['fechaNacimiento'] = StringVar()
editEntries.append(Entry(listRegistersFrame, textvariable=registroEdicion['fechaNacimiento']))

# if registroEdicion['edadCalculada'] is None:
Label(listRegistersFrame, text=str("Edad Calculada")).place(x=700, y=180)
registroEdicion['edadCalculada'] = StringVar()
Entry(listRegistersFrame, textvariable=registroEdicion['edadCalculada'], state='disabled').place(x=700, y=200)

makeEditionBtn = Button(listRegistersFrame, command=Edit, text="Actualizar", state='disabled')
makeEditionBtn.place(x=620, y=230)

cancelEditionBtn = Button(listRegistersFrame, command=deactivateEdition, text="Cancelar", state='disabled')
cancelEditionBtn.place(x=750, y=230)

#Crea dinamicamnete los Entries
incrementX = 150
xPos = 410
yPos = 50
for entry in editEntries:
    entry.config(state='disabled')
    if(xPos > 1010):
        xPos = 410
        yPos += 50
    entry.place(x=xPos, y=yPos)
    xPos += incrementX
#------------------FIN DE VISTA DE LISTADO---------------#


# Se usa geometry para dar tamaño a la ventana principal
root.geometry("1200x300")
root.mainloop()
