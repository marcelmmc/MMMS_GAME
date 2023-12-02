import logidevmon
import time

test_time = 10

waiting_for_input = input()
start_time = time.time()

def processEvents(message):
    global start_t 
    current_time = time.time()
    time_elapsed = current_time - start_time
    print (f"{time_elapsed}: {message}")
    return (time_elapsed < test_time)

mouseUnitId = 0
keyboardUnitId = 0

print ("Devices list")
logidevmon.list_devices()
for device in logidevmon.LOGITECH_DEVICES:
    print (f"{device['unitId']} {device['type']} : {device['name']}")
    
    if (device["type"] == "keyboard"):
        keyboardUnitId = device['unitId']
    
    if (device["type"] == "mouse"):
        mouseUnitId = device['unitId']

if (keyboardUnitId != 0):
    print("Set spykeys on keyboard to true")
    logidevmon.set_spyConfig(keyboardUnitId,False,True,False,False,False)
    logidevmon.read_events(processEvents)
    print ("Set spykeys to false")
    logidevmon.set_spyConfig(keyboardUnitId,False,False,False,False,False)