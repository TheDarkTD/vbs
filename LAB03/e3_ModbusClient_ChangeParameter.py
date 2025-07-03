import time
import math

from pyModbusTCP.client import ModbusClient
from time import sleep

c = ModbusClient(host="127.0.0.1", port=502, auto_open=True, auto_close=True)

x = 0.0

while True:
 x = x + 0.1
 y = 101 + math.trunc(100 * math.sin(x))
  
 rq = c.write_multiple_registers(1, [y])
 sleep(0.5)

