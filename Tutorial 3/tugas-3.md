Module Pembangkit.py berisi class Pembangkit
```py
class Pembangkit:
  
    def __init__(self, name="Unknown", type="Unknown", location="Unknown", power=0, status="Stop"):
        self.name = name
        self.type = type
        self.location = location
        self.power = power
        self.status = status
  
    def __str__(self):
        vals = ""
        vals += f"Nama              : {self.name}\n"
        vals += f"Jenis             : {self.type}\n"
        vals += f"Lokasi            : {self.location}\n"
        vals += f"Produksi Daya     : {self.power}\n"
        vals += f"Status            : {self.status}\n"
        return vals

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setType(self, type):
        self.type = type
    def getType(self):
        return self.type 
  
    def setLocation(self, location):
        self.location = location
    def getLocation(self):
        return self.location

    def setPower(self, power):
        self.power = power
    def getPower(self):
        return self.power

    def setStatus(self, status):
        self.status = status
    def getStatus(self):
        return self.status
```

Module Boiler.py berisi class Boiler
```py
class Boiler:
    
    def __init__(self, name="Unknown", temper=0, pressure=0):
        self.name = name
        self.temper = temper
        self.pressure = pressure
        
    def __str__(self):
        vals = ""
        vals += f"Nama          : {self.name}\n"
        vals += f"Temperatur    : {self.temper}\n"
        vals += f"Tekanan       : {self.pressure}\n"
        return vals
    
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setStatus(self, status):
        self.status = status
    def getStatus(self):
        return self.status

    def setTemper(self, temper):
        self.temper = temper
    def getTemper(self):
        return self.temper
    
    def setPressure(self, pressure):
        self.pressure = pressure
    def getPressure(self):
        return self.pressure
    
    def heatUp(self):
        self.setTemper(self.getTemper()+150)
        self.setPressure(self.getPressure()+80)

    def heatDown(self):
        self.setTemper(self.getTemper()-150)
        self.setPressure(self.getPressure()-80)
        if(self.getTemper()<0):
            self.setTemper(0)
            self.setPressure(0)
```

Module Turbine.py berisi class Turbine
```py
class Turbine:
    def __init__(self, name="Unknown", spin=0):
        self.name = name
        self.spin = spin
        
    def __str__(self):
        vals = ""
        vals += f"Nama          : {self.name}\n"
        vals += f"Putaran        : {self.spin}\n"
        return vals
    
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name

    def setSpin(self, spin):
        self.spin = spin
        
    def getSpin(self):
        return self.spin
```

Program utama untuk melakukan operasi starting up pembangkit
```py
import os

import Pembangkit
import Boiler
import Turbine

clear = lambda: os.system('cls')

def syncSystem(pembangkit, boiler, turbine):
    if(boiler.getTemper()==0):
        pembangkit.setStatus("Stop")
    elif(boiler.getTemper()>0):
        pembangkit.setStatus("Starting...")
        turbine.setSpin(boiler.getPressure()*8)
    elif(boiler.getTemper()>500):
        turbine.setSpin(boiler.getPressure()*8)
        
    if(turbine.getSpin()>2500):
        pembangkit.setStatus("Running...")
        pembangkit.setPower(turbine.getSpin()/100*1.5)
    else:
        pembangkit.setPower(0)

muaraKarang = Pembangkit.Pembangkit("Muara Karang", "PLTGU", "Pluit", 0)
boilerUtama = Boiler.Boiler("Boiler Utama")
turbineUtama = Turbine.Turbine("Turbin Utama")
pilih = 0
clear()
while(pilih<6):  
    print("Action:\n1. Status Pembangkit\n2. Status Boiler\n3. Status Turbin\n4. Boiler Heat Up\n5. Boiler Heat Down\n6. Exit\n")
    pilih = int(input("Pilih:"))
    if (pilih == 1): 
        clear()
        print(muaraKarang)
    elif(pilih == 2):
        clear()
        print(boilerUtama)
    elif(pilih==3):
        clear()
        print(turbineUtama)
    elif(pilih == 4):
        clear()
        boilerUtama.heatUp()
        syncSystem(muaraKarang, boilerUtama, turbineUtama)
    elif(pilih == 5):
        clear()
        boilerUtama.heatDown()
        syncSystem(muaraKarang, boilerUtama, turbineUtama)
```
