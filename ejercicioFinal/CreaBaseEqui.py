import sqlite3

con = sqlite3.connect("ServicioTec.db")
cur = con.cursor()
cur.execute("CREATE TABLE equipos (idequi INTEGER PRIMARY KEY AUTOINCREMENT, tipo TEXT, desc TEXT, acc TEXT, prob TEXT, solu TEXT)")
con.commit()
con.close()
