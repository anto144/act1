class email:
    __idCuenta = ""
    __dominio = ""
    __tipoDominio =""
    __contrasena = "1234"
    def __init__(self, idCuenta="", dominio="", tipodominio="", contrasena=""): 
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipodominio
        self.__contrasena = contrasena

    def Retornaemail(self):
        return "{}@{}.{}".format(self.__idCuenta, self.dominio,self.tipodominio) 

    def getIdCuenta (self):
        return self.__idCuenta

    def getDominio (self):
        return self.__dominio
    def getTipoDominio (self):
        return self.__tipoDominio

    def CrearCuenta(self, NuevoMail):
        arroba= NuevoMail.rfind("@")
        punto = NuevoMail.rfind(".")
        if (arroba != -1) and (punto!= -1):
            self.__idCuenta= NuevoMail[:arroba]
            self.__dominio = NuevoMail[ arroba +1 : punto]
            self.__tipoDominio= NuevoMail [punto+1 :]

    def cambiarContrasenia(self, contrasena):
        self.__contrasena = contrasena
        return self.__contrasena









