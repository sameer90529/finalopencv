# Hardware Wiring Guide - Arduino LED Controller

This guide describes the physical wiring connecting an Arduino Uno/Nano microcontroller to the emotion status LEDs.

### Pinout Mapping:
| Arduino Digital Pin | Component | Color | Resistor | Description |
|---|---|---|---|---|
| Pin 2 | 5mm LED | Green | 220 Ohm | Active when HAPPY state detected |
| Pin 3 | 5mm LED | Blue | 220 Ohm | Active when SAD state detected |
| Pin 4 | 5mm LED | Red | 220 Ohm | Active when ANGRY / High Risk state detected |
| Pin 5 | 5mm LED | Yellow | 220 Ohm | Active when SURPRISE state detected |
| Pin 6 | 5mm LED | White | 220 Ohm | Active when NEUTRAL state detected |
| GND | Common Ground | - | - | Common ground rail for all LED cathodes |

### Connection Diagram:
``
Arduino Pin 2 ----[ 220 Ohm ]---- Anode (+) [Green LED] Cathode (-) ---- GND
Arduino Pin 3 ----[ 220 Ohm ]---- Anode (+) [Blue LED]  Cathode (-) ---- GND
Arduino Pin 4 ----[ 220 Ohm ]---- Anode (+) [Red LED]   Cathode (-) ---- GND
Arduino Pin 5 ----[ 220 Ohm ]---- Anode (+) [Yel LED]   Cathode (-) ---- GND
Arduino Pin 6 ----[ 220 Ohm ]---- Anode (+) [Wht LED]   Cathode (-) ---- GND
``

### Baud Rate:
Serial communication is configured at **9600 baud**.
