import requests
from xml.dom.minidom import parse, parseString
import time

class TipoDeCambio:
    def __init__(self):
        fechaLista = time.localtime()
        self.fecha = str(fechaLista[2])+"/"+str(fechaLista[1])+"/"+str(fechaLista[0])
        #self.ObtenerTipoDeCambio()

    def ObtenerTipoDeCambio(self):
        print("holi")
        """Solicita el tipo de cambio del dólar al banco central de Costa Rica
        return [compra, venta]"""

        # URL del banco donde se va a solicitar, en este caso, el BCCR
        url = "https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicosXML"

        # Datos de la solicitud de compra
        datosCompra = {"Indicador": "317", 
        "FechaInicio":self.fecha, 
        "FechaFinal":self.fecha, 
        "Nombre": "Proyecto", 
        "SubNiveles": "N", 
        "CorreoElectronico": "proyecto3davidscoorpos@gmail.com", 
        "Token": "OT0IE3372C"}

        # Datos de la solicitud de compra
        datosVenta = {"Indicador": "318", 
        "FechaInicio":self.fecha, 
        "FechaFinal":self.fecha, 
        "Nombre": "Proyecto", 
        "SubNiveles": "N", 
        "CorreoElectronico": "proyecto3davidscoorpos@gmail.com", 
        "Token": "OT0IE3372C"}

        resultadoCompra = requests.post(url, data = datosCompra) # Envía la solicitud de compra
        resultadoVenta = requests.post(url, data = datosVenta) # Envía la solicitud de venta

        textoCompra = resultadoCompra.text # Obtiene los datos de compra como un string
        textoVenta = resultadoVenta.text # Obtiene los datos de venta como un string

        #print(textoCompra)
        #print(textoVenta)

        compra = textoCompra.split("NUM_VALOR")[1][4:-5] # Separa el  número de los datos no necesarios
        venta = textoVenta.split("NUM_VALOR")[1][4:-5] # Separa el  número de los datos no necesarios
        print(type(compra))
        compra = int(float(compra))
        return compra # Retorna los datos de compra y venta del dólar actual

    def ObtenerFecha(self):
        """Retorna la fecha actual como un string, con el formato dd/mm/aaa"""

        return self.fecha # Retorna la fecha

tipoDeCambio = TipoDeCambio() # Crea una instancia para llamar por medio de esta
