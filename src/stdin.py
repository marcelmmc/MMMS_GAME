import threading
import sys
import json

keyboard_name = None

def read_stdin():
    global keyboard_name
    while True:
        line = sys.stdin.readline()
        if not line:
            break
            
        message = line.strip()
        if not message.startswith("msg:"):
            continue

        msg = json.loads(message[4:])
        if msg["type"] == "keyboardinfo":
            keyboard_name = msg["name"]

def start_read_stdin_thread():
    threading.Thread(target=read_stdin).start()