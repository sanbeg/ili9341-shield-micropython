#! /bin/bash

mpremote=~/.local/bin/mpremote

#$mpremote mip install logging ssd1306 neopixel
#$mpremote mip install framebuf

# note can seperate commands with +

$mpremote cp ili9341.py ili9341_generic.py ili9341_stm.py :
$mpremote cp demo_stripe.py : + reset
