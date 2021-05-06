import datetime
import sys
from time import sleep

# dt = datetime.datetime.now().time()
# comp_time = dt.time()

# print(comp_time)
# stop_time = datetime.time(17, 30, 00, 000)
stop_time = datetime.time(00, 30, 00, 000)
print(stop_time)

while True:
    dt = datetime.datetime.now().time()
    if dt > stop_time:
        print('exit')
        sys.exit()
    else:
        sleep(10)
        
