class Cli:
    idcli = 0
    nom = ""
    ape =""
    cel = 0
    tel = 0
    dir = ""
    email = ""
    cuit = 0 

    def __init__(self, idcli, nom, ape, cel, tel, dir, email, cuit):
        self.idcli = idcli
        self.nom = nom
        self.ape = ape
        self.cel = cel
        self.tel = tel
        self.dir = dir
        self.email = email
        self.cuit = cuit
