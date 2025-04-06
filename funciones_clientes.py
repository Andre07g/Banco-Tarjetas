import json

def leer_clientes():
    with open ("clientes.json","r") as file:
        clientes=json.load(file)
    return clientes

clientes=leer_clientes()

def escribir_clientes():
    with open ("clientes.json","w") as file:
        json.dump(clientes, file, indent=4)

def añadir_clientes():
        cliente_existe=False
        while True:
            try:
                documento=int(input("Ingrese el documento del cliente: "))
                break
            except: print("Ingrese un documento valido")
        for cliente in clientes:
            if documento==cliente["Cedula"]:
                 cliente_existe=True
        if cliente_existe==True: print("El cliente ingresado ya existe")
        else:
            nombre=input("Ingrese el nombre del cliente: ").title()
            while True:
                try:
                    numero_contacto=int(input("Ingrese el numero telefonico del cliente: "))
                    break
                except: print("Ingrese una opciòn valida")
            while True:
                sexo=input("1.Hombre\n2.Mujer\n")
                match sexo:
                    case "1": 
                        sexo="Masculino"
                        break
                    case "2": 
                        sexo="Femenino"
                        break
                    case _: print ("Ingrese una opciòn valida")
            clientes.append({"Nombre":nombre,
                             "Cedula":documento,
                             "Numero":numero_contacto,
                             "Sexo":sexo})
            print("El cliente fue añadido correctamente")
            escribir_clientes()

def editar_clientes():
        cliente_existe=False
        while True:
            try:
                documento=int(input("Ingrese el documento del cliente: "))
                break
            except: print("Ingrese un documento valido")
        for cliente in clientes:
            if documento==cliente["Cedula"]:
                 cliente_existe=True
                 indice=clientes.index(cliente)
        if cliente_existe==False: print("El cliente ingresado no existe")
        else:
            print("==Nueva informaciòn del cliente==")
            nombre=input("Ingrese el nombre del cliente: ").title()
            while True:
                try:
                    numero_contacto=int(input("Ingrese el numero telefonico del cliente: "))
                    break
                except: print("Ingrese una opciòn valida")
            while True:
                sexo=input("1.Hombre\n2.Mujer\n")
                match sexo:
                    case "1": 
                        sexo="Masculino"
                        break
                    case "2": 
                        sexo="Femenino"
                        break
                    case _: print ("Ingrese una opciòn valida")
            clientes[indice]={"Nombre":nombre,
                             "Cedula":documento,
                             "Numero":numero_contacto,
                             "Sexo":sexo}
            print("El cliente fue editado correctamente")
            escribir_clientes()

def eliminar_clientes():
    cliente_existe=False
    while True:
            try:
                documento=int(input("Ingrese el documento del cliente: "))
                break
            except: print("Ingrese un documento valido")
    for cliente in clientes:
        if documento==cliente["Cedula"]:
            cliente_existe=True
            indice=clientes.index(cliente)
    if cliente_existe==False: print("El cliente ingresado no existe")
    else:
        while True:
            confirmacion=input("Por seguridad, escriba 'Confirmacion' para eliminar el cliente\nEscriba 'Cancelar' para cancelar la operacion: ")
            if confirmacion=="Confirmacion":
                clientes.pop(indice)
                print("El cliente fue eliminado correctamente")
                escribir_clientes()
                break
            elif confirmacion=="Cancelar": 
                print("Operaciòn cancelada")
                break
            else: print("Digite una opciòn correcta")

