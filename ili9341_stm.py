from machine import Pin
import stm


_MASKA = const((1<<8)|(1<<9)|(1<<10))
_MASKB = const((1<<3)|(1<<4)|(1<<5)|(1<<10))
_MASKC = const(1<<7)

def _outpin(pin):
    pin.init(pin.OUT)
        
class NucleoEmitter:
    @staticmethod
    def init():
        _outpin(Pin.board.D8) #LCD D0 = a9
        _outpin(Pin.board.D9) #LCD D1 = c7
        _outpin(Pin.board.D2) #LCD D2 = a10
        _outpin(Pin.board.D3) #LCD D3 = b3
        _outpin(Pin.board.D4) #LCD D4 = b5
        _outpin(Pin.board.D5) #LCD D5 = b4
        _outpin(Pin.board.D6) #LCD D6 = b10
        _outpin(Pin.board.D7) #LCD D7 = a8

    @staticmethod
    @micropython.viper
    def emit(data: int):  
        dc = 0
        da = 0
        db = 0
        d = int(data) & 0xff
        
        da = da | ((d >> 0) & 1) << (9) | ((d >> 2) & 1) << (10) | ((d >> 7) & 1) << (8)
        db = db | ((d >> 3) & 1) << (3) | ((d >> 4) & 1) << (5) | ((d >> 5) & 1) << (4) | ((d >> 6) & 1) << (10)
        dc = dc | ((d >> 1) & 1) << (7)

        da = da | (da ^ int(_MASKA)) << 16
        db = db | (db ^ int(_MASKB)) << 16
        dc = dc | (dc ^ int(_MASKC)) << 16
        
        stm.mem32[stm.GPIOA + stm.GPIO_BSRR] = da
        stm.mem32[stm.GPIOB + stm.GPIO_BSRR] = db
        stm.mem32[stm.GPIOC + stm.GPIO_BSRR] = dc
