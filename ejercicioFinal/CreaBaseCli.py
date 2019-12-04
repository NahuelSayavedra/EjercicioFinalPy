import sqlite3

con = sqlite3.connect("ServicioTec.db")
cur = con.cursor()
cur.execute("CREATE TABLE clientes (idecli INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, ape TEXT, cel TEXT, tel TEXT, drir TEXT, email TEXT, cuit TEXT)")
con.commit()
con.close()

