from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

# Create an instance of ModbusServer
server = ModbusServer("127.0.0.1", 502, no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    state = [0]
    while True:
        DataBank.set_words(0, [int(uniform(0, 10))])
        sleep(0.5)

except:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")

