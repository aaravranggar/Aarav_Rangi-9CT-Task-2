import machine
import onewire
import ds18x20
import time

def OverheatPreset():   # preset 1
    limit = 40

    # sensor setup
    ds = machine.Pin(26)
    ow = onewire.OneWire(ds)
    sensor = ds18x20.DS18X20(ow)

    # LED + buzzer
    led = machine.Pin(15, machine.Pin.OUT)
    buzzer = machine.Pin(14, machine.Pin.OUT)

    # find sensor
    roms = sensor.scan()
    print("Sensor:", roms)

    if len(roms) == 0:
        print("No sensor found")
        return

    while True:
        sensor.convert_temp()
        time.sleep_ms(750)
        temp = sensor.read_temp(roms[0])

        print("Temp:", temp)

        if temp > limit:
            led.value(1)
            buzzer.value(1)
        else:
            led.value(0)
            buzzer.value(0)

        time.sleep(5)
 