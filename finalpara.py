#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      inap
#
# Created:     14/12/2023
# Copyright:   (c) inap 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
#from bd import *
raiz = Tk()
raiz.title("Jack Panta Ramirez")



boton1=Button(raiz, text="Conectar BD")
boton1.pack( padx=10,pady=0)

boton2=Button(raiz, text="Alta")
boton2.pack( padx=20,pady=0)

boton3=Button(raiz, text="Baja")
boton3.pack( padx=30,pady=0)

boton4=Button(raiz, text="Consulta")
boton4.pack( padx=40,pady=0)

boton5=Button(raiz, text="Salir", command=raiz.destroy)
boton5.pack( padx=50,pady=0)

miFrame= Frame(raiz, width=2400, height=1200)
miFrame.pack()

cuadrocodigo=Entry(miFrame)
cuadrocodigo.grid(row=1,column=1, padx=10, pady=10)

cuadrodesc=Entry(miFrame)
cuadrodesc.grid(row=2,column=1, padx=10, pady=10)

cuadroprovee=Entry(miFrame)
cuadroprovee.grid(row=3,column=1, padx=10, pady=10)

cuadroprecio=Entry(miFrame)
cuadroprecio.grid(row=4,column=1, padx=10, pady=10)

cuadrostock=Entry(miFrame)
cuadrostock.grid(row=5,column=1, padx=10, pady=10)

cuadrostockMin=Entry(miFrame)
cuadrostockMin.grid(row=6,column=1, padx=10, pady=10)

textoComenta=Text(miFrame, width=18, height=7)
textoComenta.grid(row=7,column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComenta.yview)
scrollVert.grid(row=7,column=2, sticky="nsew")

textoComenta.config(yscrollcommand=scrollVert.set)



datosP=Label(miFrame, text="Ferreteria de los Amigos" ,font=("Comic Sans MS", 20), fg="black")
datosP.grid(row=0,column=0, padx=0, pady=0, columnspan=3)



codigoLabel=Label(miFrame, text="Codigo_ID: ")
codigoLabel.grid(row=1,column=0, sticky="w", padx=10, pady=10)


descLabel=Label(miFrame, text="Descripcion: ")
descLabel.grid(row=2,column=0, sticky="w", padx=10, pady=10)

proveeLabel=Label(miFrame, text="proveedor: ")
proveeLabel.grid(row=3,column=0, sticky="w", padx=10, pady=10)

precioLabel=Label(miFrame, text="precio unitario: ")
precioLabel.grid(row=4,column=0, sticky="w", padx=10, pady=10)

stockLabel=Label(miFrame, text="stock: ")
stockLabel.grid(row=5,column=0, sticky="w", padx=10, pady=10)

stockMinLabel=Label(miFrame, text="stock minimos: ")
stockMinLabel.grid(row=6,column=0, sticky="w", padx=10, pady=10)

comentaLabel=Label(miFrame, text="COMENTARIOS")
comentaLabel.grid(row=7,column=0)




raiz.mainloop()
