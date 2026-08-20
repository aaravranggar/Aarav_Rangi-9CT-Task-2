from machine import Pin, ADC
from time import sleep

# inputs
sensor = ADC(26)  # Potentiometer wire

# outputs
led = Pin(15, Pin.OUT)      # led long leg at GP15
buzzer = Pin(2, Pin.OUT)    # buzzer connected to GP2

# setting
THRESHOLD = 40000  # can adjust for the potentiometer

# the functions
def read_temperature():
    """Simulated temperature using potentiometer"""
    return sensor.read_u16()

def alert_on():
    """Turn on led + buzzer"""
    led.value(1)
    buzzer.value(1)

def alert_off():
    """Turn off led + buzzer"""
    led.value(0)
    buzzer.value(0)

def check_overheating():
    """Main logic for overheating detection"""
    temp = read_temperature()
    print("Temperature:", temp)

    if temp > THRESHOLD:
        alert_on()
    else:
        alert_off()

# Main loop stuff
while True:
    check_overheating()
    sleep(0.2)
