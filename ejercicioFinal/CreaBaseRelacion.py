import sqlite3

con = sqlite3.connect("ServicioTec.db")
cur = con.cursor()
cur.execute("CREATE TABLE relacion (id INTEGER PRIMARY KEY AUTOINCREMENT, idcli INTEGER NOT NULL, idequi INTEGER NOT NULL, FOREIGN KEY(idcli) REFERENCES clientes(idcli), FOREIGN KEY(idequi) REFERENCES equipos(idequi))")
con.commit()
con.close()
