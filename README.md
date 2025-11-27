This library is to support ILI9341 TFT screens on micropython.  Currently, it's primarily focused on a parallel 
interface TFT shield with a nucleo board, but it should be flexible for other use cases.

# Emitters

A key difference in different hardware configurations is in how the data is sent to the module, which depends on 
both the module and the microcontroller board.  For better flexibility this code is structured to seperate the
data passing into a seperate class called an `Emitter`, so that you can swap out different emitters without changing
other driver code.

Currently, two emitters are implemented

## GenericParallelEmitter

This emitter accepts 8 pins, and uses the standard Micropython `Pin` functionality to send the data.  This gives it the
most flexibility, since it can use any pins on any board, but at the cost of some speed as each bit has to be written individually.

```python
from ili9341 import Display
from ili9341_generic import GenericParallelEmitter
from machine import Pin

# control pins
LCD_RD = Pin.board.A0 #a0
LCD_WR = Pin.board.A1
LCD_RS = Pin.board.A2
LCD_CS = Pin.board.A3
LCD_RST = Pin.board.A4

#data pins
LCD_D0 = Pin.board.D8 #a9
LCD_D1 = Pin.board.D9 #c7
LCD_D2 = Pin.board.D2 #a10
LCD_D3 = Pin.board.D3 #b3
LCD_D4 = Pin.board.D4 #b5
LCD_D5 = Pin.board.D5 #b4
LCD_D6 = Pin.board.D6 #b10
LCD_D7 = Pin.board.D7 #a8

emitter = GenericParallelEmitter(LCD_D0, LCD_D1, LCD_D2, LCD_D3, LCD_D4, LCD_D5, LCD_D6, LCD_D7) 
lcd = Display(rst = LCD_RST, cs=LCD_CS, rs = LCD_RS, wr = LCD_WR, rd = LCD_RD, emitter = emitter)
```

## NucleoEmitter

When using this shield on a Nucleo board we have a fixed set of pins, which we can write to with some stm-specific functions.  
This gives us a nice speed up, but there's not much flexibility here, since this will only work on an STM32, and is hard-coded 
to use a specific set of pins.

```python
from ili9341 import Display
from ili9341_stm import NucleoEmitter
from machine import Pin

# control pins
LCD_RD = Pin.board.A0 #a0
LCD_WR = Pin.board.A1
LCD_RS = Pin.board.A2
LCD_CS = Pin.board.A3
LCD_RST = Pin.board.A4

emitter = NucleoEmitter()
lcd = Display(rst = LCD_RST, cs=LCD_CS, rs = LCD_RS, wr = LCD_WR, rd = LCD_RD, emitter = emitter)
```

