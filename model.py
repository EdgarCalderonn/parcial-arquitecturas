import csv



class Singleton (object):
    instance = None       
    def __new__(cls, *args, **kargs): 
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance


class Ambiente:

    tiempo = ""
    temperatura = 0.0
    humedad = 0.0


    def __init__(self,tiempo,temperatura,humedad):
        self.tiempo      = tiempo
        self.temperatura = temperatura
        self.humedad     = humedad

# Clase para manejar los datos
class Data(Singleton):
    def getData(self):    
        datos = []
        m1 = open("09052019.csv","r")
        m1_csv = csv.reader(m1)
        for tiempo,temperatura,humedad in m1_csv:
            datos.append(Ambiente(str(tiempo),temperatura,humedad))
        
        m1.close()
        
        return datos

    
    def writeData(self,tiempo,temperatura,humedad):
        
        tupla = [tiempo,temperatura,humedad]
        m = open("09052019.csv","a")
        m_write = csv.writer(m)
        m_write.writerow(tupla)
        m.close()
        return True



    
    


    

        







