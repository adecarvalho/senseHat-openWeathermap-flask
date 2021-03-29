from sense_hat import SenseHat
import os

class Capteur(object):

    def __init__(self):
        self.sense=SenseHat()
        self.datas={}
        #self.temperature=0
        #self.pressure=0
        #self.humidity=0
    
    def ajuste_temperature(self):
        temp=round(self.sense.get_temperature(),2)
        temp_cpu=self.get_cpu_temp()

        temp_cal=temp-((temp_cpu-temp)/1.5)
        return temp_cal
    
    def mesure(self):
        #self.datas["temperature"] = round(self.sense.get_temperature(),2)
        print(round(self.sense.get_temperature(),2))
        self.datas["temperature"] = round(self.ajuste_temperature(),2)
        self.datas["pressure"] = int(self.sense.get_pressure())
        self.datas["humidity"] = round(self.sense.get_humidity(),2)
    
    def get_cpu_temp(self):
        res=0
       
        if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
            print("fichier ouvert")
            with open('/sys/class/thermal/thermal_zone0/temp') as f:
                val=int(f.read()) / 1000
                print("Cpu temp= {}".format(val))
                return val
        
    
    def renderText(self, _txt):
        self.sense.show_message(_txt, text_colour=[250,20,250])
