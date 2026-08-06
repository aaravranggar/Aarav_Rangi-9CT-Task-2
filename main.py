import machine
import onewire
import ds18x20
import time

# Temperature limit
LIMIT = 40

# Sensor placement
ds = machine.Pin(26)
ow = onewire.OneWire(ds)
sensor = ds18x20.DS18X20(ow)

# LED and buzzer
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

# Find sensor
roms = sensor.scan()
print(roms)

if len(roms) == 0:
    print("No sensor found")
else:
    while True:
        sensor.convert_temp()
        time.sleep_ms(750)

        temp = sensor.read_temp(roms[0])
        print("Temp:", temp)

        if temp > LIMIT:
            led.value(1)
            buzzer.value(1)
        else:
            led.value(0)
            buzzer.value(0)

        time.sleep(5)
