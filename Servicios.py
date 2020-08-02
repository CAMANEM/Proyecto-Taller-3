import json




#servicio = # Debe ser un string de preferiblemente menos de 50 caracteres
#costo = 25000  # El costo debe ser int

class Servicios:
    def __init__(self):
        pass

    def nuevo_servicio(self, servicio, costo):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        ID_Nuevo = archivo["Proximo_ID"]
        archivo["Servicios"][ID_Nuevo] = { "descripcion": servicio, "costo": costo}  # Agrega el servicio
        archivo["ID_existentes"] = archivo["ID_existentes"] + [ID_Nuevo]  # Añade el id a la lista de ID´s existentes
        archivo["Proximo_ID"] = str(int(ID_Nuevo) + 1 )  # Suma el contador de para generar ID´s
        info = json.dumps(archivo, indent=1)
        with open("Servicios/Servicios_y_Costos.json", "w") as file:
            file.write(info)
            file.close()

    def Modificar_Servicio(self, ID, descripcion, costo):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        archivo["Servicios"][ID] = {"descripcion": descripcion, "costo": costo}
        info = json.dumps(archivo, indent=1)
        with open("Servicios/Servicios_y_Costos.json", "w") as file:
            file.write(info)
            file.close()

    def Validar_Nuevo_Servicio(self, servicio, costo):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        servicios = self.Recorre_Servicios()
        for i in servicios:
            if archivo["Servicios"][i]["descripcion"] == servicio:
                print("El servicio ingresado ya existe")
                return False
        print(True)
        return self.nuevo_servicio(servicio, costo)


    def Recorre_Servicios(self):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        lista_ID = []
        for i in archivo["ID_existentes"]:
            lista_ID += [i]
        return (lista_ID)

    def Recorre_Servicios_Descripcion(self):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        lista_servicios = self.Recorre_Servicios()
        lista_servicios_descripcion = []
        for i in lista_servicios:
            lista_servicios_descripcion += [archivo["Servicios"][i]["descripcion"]]
        return lista_servicios_descripcion

    def Limpia_Servicios_a_Facturar(self):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        archivo["Servicios a facturar"] = []
        info = json.dumps(archivo, indent=1)
        with open("Servicios/Servicios_y_Costos.json", "w") as file:
            file.write(info)
            file.close()

    def Agregar_Servicios_a_Facturar(self, descripcion_y_cant):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        IDs = self.Recorre_Servicios()
        for i in IDs:
            if archivo["Servicios"][i]["descripcion"] == descripcion_y_cant[0]:   # Busca el id del servicio a agregar
                archivo["Servicios a facturar"] += [[i]+descripcion_y_cant]
                info = json.dumps(archivo, indent=1)
                with open("Servicios/Servicios_y_Costos.json", "w") as file:
                    file.write(info)
                    file.close()
                return

        # Cuando no retrocede en el canvas llamar a estas funcion para limpiar contador
    def Obtener_Servicios_a_Facturar(self):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        servicios_a_facturar = archivo["Servicios a facturar"]
        archivo["Servicios a facturar"] = []
        info = json.dumps(archivo, indent=1)
        with open("Servicios/Servicios_y_Costos.json", "w") as file:
            file.write(info)
            file.close()
        servicios = []
        for i in servicios_a_facturar:
            servicios = servicios + [{"ID": i[0], "tipo": i[1], "cant": i[2]}]
        return servicios


servicios = Servicios()


def Reinicia_Facturas():
    data = {"N°_Factura": "1",
            "Facturas": []
            }
    info = json.dumps(data, indent=1)
    with open("Servicios/Facturas.json", "w") as file:
        file.write(info)
        file.close()
#Reinicia_Facturas()

def limpia_Servicios_y_Costos():
    data = {
            "Proximo_ID": "1",
            "Servicios a facturar": [],
            "ID_existentes": [],
            "Servicios": {}
            }
    info = json.dumps(data, indent=1)
    with open("Servicios/Servicios_y_Costos.json", "w") as file:
        file.write(info)
        file.close()

#limpia_Servicios_y_Costos()