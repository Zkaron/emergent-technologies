#! /usr/bin/env python
# Proyecto.

from Tkinter import *

def Aceptar():
    f=open('./registro2.txt','r+')
    f.write(varN.get())
    f.write(varAM.get())
    f.write(varAP.get())
    f.write(varCr.get())
    f.write(varE.get())
    f.write(varCalle.get())
    f.write(varNE.get())
    f.write(varNI.get())
    f.write(varCol.get())
    f.write(varM.get())
    f.write(varEst.get())
    f.write(varCP.get())
    f.write(varT.get())
    f.write(varEmail.get())
    f.write(varFN.get())

ventana = Frame(height=500,width=510)
ventana.pack(padx=(50,50),pady=(10,10))

lbTitulo = Label(text="CONTESTA EL FORMULARIO").place(x= 250,y=50)

lbNom = Label(text="Nombre").place(x= 100,y=150)
varN = StringVar()
camNom = Entry(ventana,textvariable=varN).place(x=50,y=115)

lbNom = Label(text="Apellido Matreno").place(x=250,y=150)
varAM = StringVar()
camAM = Entry(ventana,textvariable=varAM).place(x=200,y=115)

lbNom = Label(text="Apellido Paterno").place(x=400,y=150)
varAP = StringVar()
camAP = Entry(ventana,textvariable=varAP).place(x=350,y=115)

lbNom = Label(text="Cargo").place(x= 100,y=200)
varCr = StringVar()
camCr = Entry(ventana,textvariable=varCr).place(x=50,y=165)

lbNom = Label(text="Empresa").place(x=250,y=200)
varE = StringVar()
camE = Entry(ventana,textvariable=varE).place(x=200,y=165)

lbNom = Label(text="Calle").place(x= 100,y=250)
varCalle = StringVar()
camCalle = Entry(ventana,textvariable=varCalle).place(x=50,y=215)

lbNom = Label(text="NumeroExt").place(x=250,y=250)
varNE = StringVar()
camNE = Entry(ventana,textvariable=varNE).place(x=200,y=215)

lbNom = Label(text="NumeroInt").place(x=400,y=250)
varNI = StringVar()
camNI = Entry(ventana,textvariable=varNI).place(x=350,y=215)

lbNom = Label(text="Colonia").place(x= 100,y=300)
varCol = StringVar()
camCol = Entry(ventana,textvariable=varCol).place(x=50,y=265)

lbNom = Label(text="Municipio").place(x=250,y=300)
varM = StringVar()
camM = Entry(ventana,textvariable=varM).place(x=200,y=265)

lbNom = Label(text="Estado").place(x=400,y=300)
varEst = StringVar()
camEst = Entry(ventana,textvariable=varEst).place(x=350,y=265)

lbNom = Label(text="CodigoPostal").place(x= 100,y=350)
varCP = StringVar()
camCP = Entry(ventana,textvariable=varCP).place(x=50,y=315)

lbNom = Label(text="Telefono").place(x=250,y=350)
varT = StringVar()
camT = Entry(ventana,textvariable=varT).place(x=200,y=315)

lbNom = Label(text="CorreoElectronico").place(x=400,y=350)
varEmail = StringVar()
camEmail = Entry(ventana,textvariable=varEmail).place(x=350,y=315)

lbNom = Label(text="FechaNacimiento").place(x= 250,y=400)
varFN = StringVar()
camFN = Entry(ventana,textvariable=varFN).place(x=200,y=365)

boton = Button(ventana,command=Aceptar, text="Aceptar").place(x=200,y=450)
ventana.mainloop()
