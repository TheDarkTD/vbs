import time
from pyModbusTCP.client import ModbusClient

# init modbus client
c = ModbusClient(host="127.0.0.1", port=502, auto_open=True, auto_close=True)

# main read loop
while True:
    # read 10 registers at address 0, store result in regs list
    regs_l = c.read_holding_registers(0, 10)

    # if success display registers
    if regs_l:
        print('reg ad #0 to 9: %s' % regs_l)
        new_pv = regs_l[1] if len(regs_l) > 1 else "N/A"
        print('pv = ' + str(new_pv))
    else:
        print('unable to read registers')

    # sleep 0.5s before next polling
    time.sleep(0.5)