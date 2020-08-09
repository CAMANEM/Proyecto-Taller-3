from tkinter import messagebox
import json


class Servicios:
    def __init__(self):
        pass

    def nuevo_servicio(self, servicio, costo):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        ID_Nuevo = archivo["Proximo_ID"]
        archivo["Servicios"][ID_Nuevo] = { "descripcion": servicio, "costo": costo}  # Agrega el servicio
        archivo["ID_existentes"] = archivo["ID_existentes"] + [ID_Nuevo]  # Añade el id a la lista de ID´s existentes
        archivo["Proximo_ID"] = str(int(ID_Nuevo) + 1 )  # Suma el contador para generar ID´s
        info = json.dumps(archivo, indent=1)
        with open("Servicios/Servicios_y_Costos.json", "w") as file:
            file.write(info)
            file.close()

    def Modificar_Servicio(self, ID, descripcion, costo):
        try:
            if costo != "" and int(costo) > 0:  ## Modifica el servicio si el nuevo costo es mayor a 0
                archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
                archivo["Servicios"][ID] = {"descripcion": descripcion, "costo": costo}
                info = json.dumps(archivo, indent=1)
                with open("Servicios/Servicios_y_Costos.json", "w") as file:
                    file.write(info)
                    file.close()
            else:
                messagebox.showinfo("Error de dato", "Hay un error en los datos ingresados")
        except:
            messagebox.showinfo("Error de datos", "Hay un error en los datos ingresados")


    def Validar_Nuevo_Servicio(self, servicio, costo):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        servicios = self.Recorre_Servicios()
        for i in servicios: # Recorre los los servicios existentes asegurandose de que no existan otros servicios con la misma descripción que el servicio a agregar
            if archivo["Servicios"][i]["descripcion"] == servicio:
                print("El servicio ingresado ya existe")
                return False
        return self.nuevo_servicio(servicio, costo)


    def Recorre_Servicios(self):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        lista_ID = []
        for i in archivo["ID_existentes"]:  # Obtiene las ID de los servicios existentes, para mostrarlas en cascada en la interfaz
            lista_ID += [i]
        return (lista_ID)

    def Recorre_Servicios_Descripcion(self):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        lista_servicios = self.Recorre_Servicios()
        lista_servicios_descripcion = []
        for i in lista_servicios:  # Obtiene las descripciones de los servicios existentes, para mostrarlas en cascada en la interfaz
            lista_servicios_descripcion += [archivo["Servicios"][i]["descripcion"]]
        return lista_servicios_descripcion

    # Reinicia una lista que contiene los servicios listados para facturar
    def Limpia_Servicios_a_Facturar(self):
        archivo = json.load(open("Servicios/Servicios_y_Costos.json"))
        archivo["Servicios a facturar"] = []
        info = json.dumps(archivo, indent=1)
        with open("Servicios/Servicios_y_Costos.json", "w") as file:
            file.write(info)
            file.close()

    # Agrega el servicio deseado a una lista con los servicios a facturar
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


servicios = Servicios()  # Instancia para utilizar los metodos de la clase

# Reinicia conpletamente las facturas en memoria
def Reinicia_Facturas():
    data = {"N°_Factura": "1",
            "Facturas": []
            }
    info = json.dumps(data, indent=1)
    with open("Servicios/Facturas.json", "w") as file:
        file.write(info)
        file.close()
#Reinicia_Facturas()

# Reinicia los servicios y costos
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