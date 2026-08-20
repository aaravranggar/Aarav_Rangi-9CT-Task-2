from machine import Pin, ADC
from time import sleep

# inputs
sensor = ADC(26)  # Potentiometer

# outputs
led = Pin(15, Pin.OUT)      # led long leg 
buzzer = Pin(2, Pin.OUT)    # buzzer 

# setting
THRESHOLD = 40   # 40°C overheating threshold

# convert ADC → Celsius (fake temperature)
def adc_to_celsius(adc_value):
    
    return (adc_value / 65535) * (100 - 20) + 20

def read_temperature():
    raw = sensor.read_u16()
    temp_c = adc_to_celsius(raw)
    return temp_c

def alert_on():
    led.value(1)
    buzzer.value(1)

def alert_off():
    led.value(0)
    buzzer.value(0)

def check_overheating():
    temp = read_temperature()
    print("Temperature (°C):", round(temp, 2))

    if temp > THRESHOLD:
        alert_on()
    else:
        alert_off()

while True:
    check_overheating()
    sleep(0.2)
