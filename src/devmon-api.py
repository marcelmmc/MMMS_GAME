#!/usr/bin/env python

import logidevmon
import sys
import os
import threading
import asyncio

keyboardUnitId = 0

print ("Devices list")
logidevmon.list_devices()
for device in logidevmon.LOGITECH_DEVICES:
    print (f"{device['unitId']} {device['type']} : {device['name']}")
    
    if (device["type"] == "keyboard"):
        keyboardUnitId = device['unitId']

if (keyboardUnitId != 0):
    print ("Set spykeys on keyboard to true")
    logidevmon.set_spyConfig(keyboardUnitId,False,True,False,False,False)

    read_events_task = None
    subprocess_task = None
    async def start_game():
        global child
        # start the game
        child = await asyncio.create_subprocess_exec(
            sys.executable,
            os.path.join(
                os.path.dirname(__file__),
                "TestGame.py" #./TestGame.py
            ),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.PIPE,
        )

        await child.wait()

        read_events_task.cancel()

    child = None
    def handleEvent(message):
        print (message)
        return child.returncode is not None

    async def run_tasks():
        global subprocess_task, read_events_task
        subprocess_task = asyncio.create_task(start_game())
        read_events_task = logidevmon.create_read_events_task(handleEvent)
        try:
            await asyncio.gather(read_events_task, subprocess_task)
        except asyncio.CancelledError:
            exit(child.returncode)

    asyncio.run(run_tasks())
    
    print ("Set spykeys to false")
    logidevmon.set_spyConfig(keyboardUnitId, False, False, False, False, False)

print ("End")