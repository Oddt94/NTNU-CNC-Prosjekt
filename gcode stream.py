import serial
import time

# Open grbl serial port ==> CHANGE THIS BELOW TO MATCH YOUR USB LOCATION
port = 'COM1'
s = serial.Serial(port, 115200)  # GRBL operates at 115200 baud. Leave that part alone.

# Open g-code file
f = open('grbl.gcode','r')

# Wake up grbl
s.write("\r\n\r\n")
time.sleep(2)   # Wait for grbl to initialize
s.flushInput()  # Flush startup text in serial input

# Stream g-code to grbl
for line in f:
    l = line.strip() # Strip all EOL characters for consistency
    print('Sending: ' + l),
    s.write(l + '\n') # Send g-code block to grbl
    grbl_out = s.readline() # Wait for grbl response with carriage return
    print(' : ' + grbl_out.strip())

# Wait here until grbl is finished to close serial port and file.
raw_input = input("  Press <Enter> to exit and disable grbl.")

# Close file and serial port
f.close()
s.close()