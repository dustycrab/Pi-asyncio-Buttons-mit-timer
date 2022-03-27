# wieder inet testen

from gpiozero import LED
from gpiozero import Button
import time
import threading
import asyncio

button_b = Button(22)
button_g = Button(27)
button_y = Button(17)
button_r = Button(4)

led_b = LED(25)
led_g = LED(24)
led_y = LED(23)
led_r = LED(18)

    
async def led_blue():
    if button_b.is_pressed:
        led_b.off()
    else:
        led_b.on()
        await asyncio.sleep(2)

async def led_green():
    if button_g.is_pressed:
        led_g.off()
    else:
        led_g.on()
        #await asyncio.sleep(2)

async def led_yellow():
    if button_y.is_pressed:
        led_y.off()
    else:
        led_y.on()
        await asyncio.sleep(2)

async def led_red():
    if button_r.is_pressed:
        led_r.off()
    else:
        led_r.on()
        await asyncio.sleep(2)

async def main():
    while True:
        await asyncio.gather(
            led_blue(),
            led_green(),
            led_yellow(),
            led_red(),
            )

if __name__ ==  '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
time.sleep(0.01)