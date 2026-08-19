from machine import Pin, ADC
from time import sleep

# inputs
sensor = ADC(26)  # Potentiometer on Point26

# outputs
led = Pin(3, Pin.OUT)
buzzer = Pin(2, Pin.OUT)

# setting
THRESHOLD = 40000  # ned to adjust for the potentiometer

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
