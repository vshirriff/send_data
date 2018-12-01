# send data collected by atlas scientific sensor to Raspberry Pi
# to https://dweet.io/. an IoT on cloud
# with thing name= pH_sensor

#check out the dweet at https://dweetpro.io/dweet/for/pH_sensor

import os
import requests

dweetIO = "https://dweetpro.io/dweet/for/"
myName = "pH_sensor"
myKey = "5Chio-8jwkT-5Akzy-Eav2g-Bq8-W"

pHC = [ ]

while True:
    ospH = os.popen('pH_sensor Chio-8jwkT-5Akzy-Eav2g-Bq8-W').readline()
    pH = (ospH.replace("pH=", "").replace(" 'C\n", ""))
    print(pH)
    pHC.append(pH)
    pHC.pop(0)

    #send to dweet.io
    rqsString = dweetIO+myName+'?'+myKey+'='+str(pH)
    print(rqsString)
    rqs = requests.get(rqsString)
    print (rqs.status_code)
    print (rqs.headers)
    print (rqs.content)