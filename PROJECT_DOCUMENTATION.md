# Aarav_Rangi-9CT-TASK-2

Assessment Task 2

## Problem

Gaming PCs and school computers get very hot when running heavy games or programs. If a cooling fan breaks or gets blocked by dust, the computer can overheat. This causes the computer to slow down, crash suddenly, or even break permanently. Users often do not realize their PC is overheating until it is too late.



## Solution

I will build a PC Overheating Alert System using a Raspberry Pi Pico to solve this problem. 

### How It Works:
* The Sensor: A digital temperature sensor will be placed near the computer's exhaust fan to measure the hot air coming out.
* The Controller: The Raspberry Pi Pico will check the temperature sensor every second.
* The Alarm: If the air gets too hot (above 40°C), the Pico will automatically flash a bright Red LED and make a loud beeping sound with a Piezo Buzzer. 

This gives the user an immediate warning so they can save their work, turn off the computer, and fix the cooling problem before anything breaks.

### Functional Requirements
* The system must read an input value from a sensor (potentiometer acting as temperature).

* The system must activate a red LED when overheating is detected.

* The system must activate a buzzer when overheating is detected.

* The system must turn off the LED and buzzer when temperature returns to safe levels.

* The system must continuously monitor the sensor in a loop.

* The system must print sensor values for testing and debugging.

### Non‑Functional Requirements
*The system must respond quickly (under 2 seconds).

* The system must be easy to assemble on a breadboard.

* The system must be reliable and run without crashing.

* The system must be safe to operate with low‑voltage components.

* The code must be simple, readable, and well‑commented.

* The system must be small enough to sit next to a PC or laptop.


## Key Actions

- Detect the current “temperature” level using a potentiometer.
- Compare the sensor value to a preset threshold.
- Turn on a red LED when overheating is detected.
- Activate a buzzer when overheating is detected.
- Turn off the LED and buzzer when temperature returns to safe levels.


## Test Cases

| Test Case            | Input                                 | Expected Output                         |
|----------------------|----------------------------------------|------------------------------------------|
| Temperature normal   | Potentiometer below threshold          | LED off, buzzer off                      |
| Temperature high     | Potentiometer above threshold          | LED on, buzzer on                        |
| Rapid change         | Potentiometer quickly turned high/low  | LED/buzzer respond within 2 seconds      |
| Debug output         | Any potentiometer value                | Console prints current sensor reading    |


