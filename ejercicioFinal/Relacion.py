import sqlite3

from Clientes import *
from equipos import *




def nequipo():
    tipo = input('Tipo de Equipo:  ')
    acc = input('Ingrese accesorios incuidos: ')
    desc = input('Describa estado del equipo: ')
    prob = input('Describa problema del equipo: ')
    agregar_equi(tipo, acc, desc, prob)


def agregar_equi(tipo, acc, desc, prob):
    try: 
        con = sqlite3.connect("ServicioTec.db")
        cur = con.cursor()
        cur.execute("INSERT INTO equipos VALUES (null, ?, ?, ?, ?)", (tipo, acc, desc, prob))
        con.commit()
        con.close()
        print("Datos Ingresados")

    except:
        print("Segui participando ")



