import logidevmon
import time
import json
import pprint
import convert

pp = pprint.PrettyPrinter(indent=2)

test_time = 30

waiting_for_input = input()
start_time = time.time()

unprocessed_key_presses = []

def processEvents(message):
    global start_t 
    current_time = time.time()
    time_elapsed = current_time - start_time
    decoded = json.loads(message)
    info = (time_elapsed, decoded['value']['pressed'], decoded['value']['vkey'])
    unprocessed_key_presses.append(info)
    print(f"{info}")
    print (f"{time_elapsed}: {message}")
    return (time_elapsed < test_time)

mouseUnitId = 0
keyboardUnitId = 0
keyboard_name = ""

print ("Devices list")
logidevmon.list_devices()
for device in logidevmon.LOGITECH_DEVICES:
    print (f"{device['unitId']} {device['type']} : {device['name']}")
    
    if (device["type"] == "keyboard"):
        keyboardUnitId = device['unitId']
        keyboard_name = device['name']
    
    if (device["type"] == "mouse"):
        mouseUnitId = device['unitId']

if (keyboardUnitId != 0):
    print("Set spykeys on keyboard to true")
    logidevmon.set_spyConfig(keyboardUnitId,False,True,False,False,False)
    logidevmon.read_events(processEvents)
    print ("Set spykeys to false")
    logidevmon.set_spyConfig(keyboardUnitId,False,False,False,False,False)

pp.pprint(unprocessed_key_presses)

print(20 * "-")

processed_key_presses = convert.process_keypresses(unprocessed_key_presses, keyboard_name)
pp.pprint(processed_key_presses)

waiting_for_input = input()