from datetime import date, timedelta
from datetime import timedelta
from tkinter import messagebox
import json
import os

class Administrar_Facturas():

    def __init__(self):
        pass

    # E: una fecha inicial y una fecha final
    # S: los datos de las facturas en ese rango de fechas y la suma del precio a pagar de las mismas
    # Orden de datos retornados ([n_factura, cliente y total_por_factura], Total_facturas)
    def Buscar_por_Fechas(self,fecha_inicial, fecha_final):
        fecha_inicial = date(fecha_inicial[0], fecha_inicial[1],fecha_inicial[2])  #date(año,mes,dia)
        fecha_final = date(fecha_final[0], fecha_final[1], fecha_final[2])
        rango = self.Obtener_Fechas(fecha_inicial, fecha_final - fecha_inicial)
        facturas = json.load(open("Servicios/Facturas.json"))["Facturas"]
        facturas_a_mostrar = []
        total = 0
        for factura in facturas:  # Explora las facturas, busca las facturas cuyas fechas se encuentren en el rango dado
            if factura["Fecha"] in rango:
                facturas_a_mostrar += [[factura["N°_Factura"], factura["Cliente"], str(factura["Total"]), factura["Vencimiento"]]]  # Guarda los datos de las facturas que se deben mostrar al usuario
                total += factura["Total"] # Suma el precio de cada factura para calcular un total por todas
        print(facturas_a_mostrar)
        print(total)
        return facturas_a_mostrar, total


    #  Axiliar de Buscar_por_Fechas e Informe_Fechas
    #  E: la fecha inicial y la cantidad de días entre la fecha inicial y final
    #  S: una lista con las fechas que se encuentran en el rango de tiempo deseado
    def Obtener_Fechas(self, fecha_inicial, rango):
        lista_fechas = []
        for i in range(rango.days + 1): # Crea una lista con las fechas que se encuentran en el rango dado
            lista_fechas += [(fecha_inicial + timedelta(days=i)).strftime("%d/%m/%Y")]
        return lista_fechas

    #  Cumple la funcion de mostra para eliminar
    #  E: Ninguna
    #  S: Muestra el nombre del cliente, el numero de consecutivo y el monto a pagar de todas las facturas. Orden ascendente
    def Mostrar_Todas(self):
        registro = json.load(open("Servicios/Facturas.json"))["Facturas"]
        facturas = []
        for factura in registro: # Crea una lista de todas las facturas con los datos de N° Factura, "Cliente" y Total
            facturas += [[factura["N°_Factura"], factura["Cliente"], str(factura["Total"])]]
        return facturas


    #  E: una lista con las ID de las facturas a eliminar
    #  S: Elimina los pdf y datos almacenados de dichas facturas
    def Eliminar(self, lista):
        registro = json.load(open("Servicios/Facturas.json"))
        facturas_a_conservar = []
        for factura in registro["Facturas"]:  #  Recorre los datos de todas las facturas
            if factura["N°_Factura"] in lista:  # Si el numero de factura que se está leyendo, se encuentra en la lista de facturas a eliminar; Elimina el pdf
                os.remove("Servicios/Invoices/" + factura["N°_Factura"] + ".pdf")
            else:
                facturas_a_conservar += [factura]  #  Si la factura leida no se encuentra en la lista de facturas a eliminar, la agrega a otra lista, que contiene las facturas que no debían ser eliminadas
        registro["Facturas"] = facturas_a_conservar  # Realiza el cambio de facturas contenidas en el archivo, excluyendo las facturas eliminadas
        info = json.dumps(registro, indent=1)
        with open("Servicios/Facturas.json", "w") as file:
            file.write(info)
            file.close()

    #  E: Ninguna
    #  S: precio total a pagar por todas las facturas y precio de sumar todos los impuestos
    def Informe_General(self):
        registro = json.load(open("Servicios/Facturas.json"))["Facturas"]
        impuestos = 0
        total = 0
        for factura in registro:  # Por cada factura guardada, suma su monto total a pagar en una variable y suma los impuestos a pagar en otra
            total += factura["Total"]
            impuestos += factura["Total"] + factura["Subtotal"]
        return (total, impuestos)


    #  E: una fecha inicial y una fecha final
    #  S: total a pagar por todas las facturas en ese rango de fechas y tambien el total de impuestos
    def Informe_Fechas(self, fecha_inicial, fecha_final):
        try:
            fecha_inicial = date(int(fecha_inicial[0]), int(fecha_inicial[1]), int(fecha_inicial[2]))  # date(año,mes,dia)
            fecha_final = date(int(fecha_final[0]), int(fecha_final[1]), int(fecha_final[2]))  #  Convierte los strings ingresados a fechas
            rango = self.Obtener_Fechas(fecha_inicial, fecha_final - fecha_inicial)  # Obtiene las fechas presentes entre el rango de fechas dado
            registro = json.load(open("Servicios/Facturas.json"))["Facturas"]
            impuestos = 0
            total = 0
            for factura in registro: #  Lee las fechas de las facturas guardadas y si coinciden con el rango de fechas a comparar suma su total e impuestos
                if factura["Fecha"] in rango:
                    total += factura["Total"]
                    impuestos += factura["Total"] + factura["Subtotal"]
            print(total, impuestos)
            return (total, impuestos)
        except:
            return

    # Abre la factura deseada
    def Mostrar_PDF(self, n_factura):
        os.startfile("Servicios\\Invoices\\" + n_factura + ".pdf")

Facturas = Administrar_Facturas() # Instancia usada para emplear los métodos de la clase



