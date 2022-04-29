import csv
from Email import email
if __name__=='__main__':
    print("Ingrese el nombre")
    nombre=input()
    print("Ingrese Identificador de Cuenta")
    id=input()
    print("Ingrese el dominio")
    dominio=input()
    print("Ingrese el  tipo de dominio")
    tipo=input()
    cuenta = email(id, dominio, tipo)
    print ("Estimado {}, te enviaremos el mensaje a la direccion de correo {}@{}.{}".format (nombre, cuenta.getIdCuenta(), cuenta.getDominio(), cuenta.getTipoDominio()))
    print("Ingrese su contrasena")
    contrasena= input()
    print ("Contraseña cambiada con exito")
    e1 = email ("Juan", "gmail", "com")
    print ("Correo: {}@{}.{}".format (e1.getIdCuenta(), e1.getDominio(), e1.getTipoDominio()))

    archivo = open ("emails.csv")
    reader = csv.reader(archivo, delimiter = ";")
    IDPrueba = input("Ingrese ID que desea verificar /n ")
    mailItem4 = email()
    cont=0
    for comp in reader:
        for i in range(10):
            mailItem4.CrearCuenta(comp[i])
            ident = mailItem4.getIdCuenta()
            if IDPrueba == ident:
                cont += 1
    print("Hay {} email con el ID {}".format(cont, IDPrueba))
    archivo.close()
