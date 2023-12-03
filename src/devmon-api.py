#!/usr/bin/env python

import logidevmon
import sys
import os
import asyncio
import json
import time
from data_save import run_save
import convert
import subprocess

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
        global child, start_time
        # start the game
        child = await asyncio.create_subprocess_exec(
            sys.executable,
            "-u", # do not buffer stdout
            os.path.join(
                os.path.dirname(__file__),
                "TestGame.py" #./TestGame.py
            ),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
            stdin=asyncio.subprocess.PIPE,
        )

        while True:
            line = await child.stdout.readline()
            if not line:
                break

            message = line.decode("utf-8").strip()
            print(message)
            if not message.startswith("msg:"):
                continue

            msg = json.loads(message[4:])
            if msg["type"] == "ready":
                m = json.dumps({
                    "type": "keyboardinfo",
                    "name": logidevmon.LOGITECH_DEVICES[0]["name"],
                })
                child.stdin.write(bytes(f"msg:{m}\n", "utf-8"))
                continue
            elif msg["type"] == "start_test":
                # do something...
                start_time = time.time()
                unprocessed_key_presses.clear()
                # msg.sentence
                # msg.dictionary
                continue
            elif msg["type"] == "quit":
                child.kill()
                continue
            elif msg["type"] == "end_test":
                # do something...

                # msg.sentence
                # msg.dictionary
                await asyncio.sleep(.2)
                child.kill()
                # display statistics
                continue

        read_events_task.cancel()

    child = None
    start_time = time.time()
    unprocessed_key_presses = []
    def handleEvent(message):
        time_elapsed = time.time() - start_time
        decoded = json.loads(message)
        info = (time_elapsed, decoded['value']['pressed'], decoded['value']['vkey'])
        unprocessed_key_presses.append(info)
        print(f"{info}")
        print (f"{time_elapsed}: {message}")
        return child.returncode is None

    async def run_tasks():
        global subprocess_task, read_events_task
        subprocess_task = asyncio.create_task(start_game())
        read_events_task = logidevmon.create_read_events_task(handleEvent)
        try:
            await asyncio.gather(read_events_task, subprocess_task)
        except asyncio.CancelledError:
            #exit(child.returncode)
            pass

    asyncio.run(run_tasks())

    print(unprocessed_key_presses)
    processed_key_presses = convert.process_keypresses(unprocessed_key_presses, logidevmon.LOGITECH_DEVICES[0]["name"])
    processed_key_presses = [i for i in processed_key_presses if i is not None] # remove None
    print(processed_key_presses)
    run_save(processed_key_presses)

    subprocess.run([
        sys.executable,
        os.path.join(
            os.path.dirname(__file__),
            "visualisation_script.py"
        ),
    ])
    
    print ("Set spykeys to false")
    try:
        logidevmon.set_spyConfig(keyboardUnitId, False, False, False, False, False)
    except:
        pass

print ("End")