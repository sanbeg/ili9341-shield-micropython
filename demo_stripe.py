from ili9341 import Display, Colors
from ili9341_stm import NucleoEmitter
from ili9341_generic import GenericParallelEmitter

from machine import Pin
from time import sleep_ms, ticks_ms

LCD_RD = Pin.board.A0 #a0
LCD_WR = Pin.board.A1
LCD_RS = Pin.board.A2
LCD_CS = Pin.board.A3
LCD_RST = Pin.board.A4

lcd = Display(rst = LCD_RST, cs=LCD_CS, rs = LCD_RS, wr = LCD_WR, rd = LCD_RD, emitter = NucleoEmitter())

def demo():
    start = ticks_ms()
    lcd.draw_rect(0,0,40,240, Colors.WHITE)# white
    lcd.draw_rect(40,0,40,240, Colors.YELLOW)# yellow
    lcd.draw_rect(80,0,40,240, Colors.CYAN)# cyan
    lcd.draw_rect(120,0,40,240, Colors.GREEN)# green
    lcd.draw_rect(160,0,40,240, Colors.MAGENTA)# magenta
    lcd.draw_rect(200,0,40,240, Colors.RED)# red
    lcd.draw_rect(240,0,40,240, Colors.BLUE)# blue
    lcd.draw_rect(280,0,40,240, Colors.BLACK)# BLACK
    
    print(f"Elapsed time ms={ticks_ms()-start}")

def restart(speed = True):   
    lcd.init()
    demo()