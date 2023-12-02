import time
import websockets

# test duration in seconds
TEST_DURATION = 5

waiting_for_input = input()
start_time = time.time()

while True:
    print("Running")

    current_time = time.time()
    time_elapsed = current_time - start_time
    print(f"Time elapsed: {time_elapsed}")

    hello()
    
    if time_elapsed >= TEST_DURATION:
        break