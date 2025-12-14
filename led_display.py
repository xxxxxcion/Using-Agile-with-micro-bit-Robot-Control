from microbit import *

# Initialize Serial (UART)
# Adjust tx/rx pins if needed based on your specific expansion board
# Usually pin1/pin2 or pin8/pin12
uart.init(baudrate=115200, tx=pin1, rx=pin2) 

display.show(Image.HAPPY) # Startup indicator

while True:
    if uart.any():
        # Read incoming data from AI Lens
        incoming = uart.read()
        if incoming:
            try:
                text = str(incoming, 'UTF-8')
                
                # Protocol logic: check for "Y" (Yes/Recognized) or "N" (No)
                if "Y" in text:
                    # Parse ID (Simplified logic)
                    if "01" in text:
                        display.show("1")
                    elif "02" in text:
                        display.show("2")
                    elif "00" in text:
                        display.show("0")
                    else:
                        display.show(Image.YES)
                elif "N" in text:
                    display.show(Image.NO)
            except:
                pass # Ignore bad data
            
    sleep(100)
