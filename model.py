import csv

class Modelo:
    tiempo = ""
    temperatura = 0.0
    humedad = 0.0

    def __init__(self,tiempo,temperatura,humedad):
        self.tiempo      = tiempo
        self.temperatura = temperatura
        self.humedad     = humedad

    @staticmethod
    def getData():    
        datos = []
        m1 = open("09052019.csv","r")
        m1_csv = csv.reader(m1)
        for tiempo,temperatura,humedad in m1_csv:
            datos.append(Modelo(str(tiempo),temperatura,humedad))
        
        m1.close()
        
        return datos

    @staticmethod
    def writeData(tiempo,temperatura,humedad):
        
        tupla = [tiempo,temperatura,humedad]
        m = open("09052019.csv","a")
        m_write = csv.writer(m)
        m_write.writerow(tupla)
        m.close()
        return True

    

        







