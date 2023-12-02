import logidevmon
import time
import asyncio

test_time = 5

waiting_for_input = input("Press any enter to start test")
start_time = time.time()
def processEvents(message):
    global start_time
    current_time = time.time()
    time_elapsed = current_time - start_time
    print (f"{time_elapsed}: {message}")
    return (time_elapsed < test_time)

def timing():
    global start_time
    current_time = time.time()
    time_elapsed = current_time - start_time
    print (f"{time_elapsed}")
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
    try:
        logidevmon.read_events_time(processEvents,test_time)
    except asyncio.TimeoutError:
        pass
    ##logidevmon.read_events_time(processEvents,test_time)
    print ("Set spykeys to false")
    logidevmon.set_spyConfig(keyboardUnitId,False,False,False,False,False)