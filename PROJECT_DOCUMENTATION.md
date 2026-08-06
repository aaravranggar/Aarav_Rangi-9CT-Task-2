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
