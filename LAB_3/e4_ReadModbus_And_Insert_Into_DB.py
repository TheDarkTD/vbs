import time
from pyModbusTCP.client import ModbusClient
import sqlite3
from datetime import datetime

def read_modbus_and_insert_to_db(database_name):
    # Initialize Modbus client
    c = ModbusClient(host="127.0.0.1", port=502, auto_open=True, auto_close=True)

    # Connect to the SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS NIVEL (
            id INTEGER PRIMARY KEY,
            value REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()

    try:
        while True:
            regs_l = c.read_holding_registers(0, 10)

            if regs_l:
                new_pv = regs_l[1] if len(regs_l) > 1 else None
                
                if new_pv is not None:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
                    # Insert the data into the database
                    cursor.execute('INSERT INTO NIVEL (value, timestamp) VALUES (?, ?)', (new_pv, timestamp))
                    conn.commit()
                    print(f"Inserted value: {new_pv} at {timestamp}")
                else:
                    print("Invalid value read from Modbus")
            else:
                print("Unable to read registers")

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        # Close the database connection and Modbus client
        conn.close()
        c.close()

# Call the function with the database name
read_modbus_and_insert_to_db("database.db")
