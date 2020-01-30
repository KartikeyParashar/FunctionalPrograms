import time

time_start_input = input("Enter 'Start' to start the time: ")
start = time.time()


time_start_output = input("Enter 'End' to end the time: ")
end = time.time()

elapsed_time = end - start
print(f"Elapsed time is: {elapsed_time}")

