from time import sleep_ms

def _outpin(pin):
    pin.init(pin.OUT)
    return pin

class Display:
    def __init__(self, emitter, rst, cs, rs, wr, rd):
        self._rst = _outpin(rst)
        self._cs = _outpin(cs)
        self._rs = _outpin(rs)
        self._wr = _outpin(wr)
        self._rd = _outpin(rd)
        self._emitter = emitter
        
        emitter.init()
        
    def _lcd_write(self, data):
        self._wr.off()
        self._emitter.emit(data)
        self._wr.on()

    def cmd_write(self, d):
        self._rs.off()
        self._lcd_write(d)
        
    def data_write(self, d):
        self._rs.on()
        self._lcd_write(d)
        
    def cmd_data(self, cmd, *data):
        self._rs.off()
        self._lcd_write(cmd)

        self._rs.on()
        for d in data:
            self._lcd_write(d)

    def clear(self, color):
        self.cmd_data(0x2a, 0, 0, 0, 0xEC)
        self.cmd_data(0x2b, 0, 0, 1, 0x3f)
        self.cmd_data(0x2c, color)

        wr = self._wr
        for y in range(0, 38400): # 240*320/2
            for z in range(0, 84):
                wr.off()
                wr.on()

    def init(self):
        rst = self._rst
        
        rst.on()
        sleep_ms(10)
        rst.off()
        sleep_ms(20)
        rst.on()
        sleep_ms(20)
        
        self._cs.on()
        self._wr.on()
        self._rd.on()
        self._cs.off()

        self.cmd_data(0x7f, 0x20) # pump ratio control
        self.cmd_data(0x3a, 0x55) # colmod pixel format
        self.cmd_data(0x36, 0b00001000) # memory access control
        self.cmd_write(0x11) # sleep out
        self.cmd_write(0x29) # display on
        
        sleep_ms(50)
        
    def draw_rect(self, col, row, width, height, color):
        self.cmd_data(0x2a, row >> 8, row & 0xFF, ((row+height-1) >> 8), ((row+height-1) & 0xFF))
        self.cmd_data(0x2b, col >> 8, col & 0xFF, ((col+width-1) >> 8), ((col+width-1) & 0xFF))
     
        lcd_write = self._lcd_write
        chigh = color >> 8
        clow = color & 0xFF

        self.cmd_data(0x2c)
        for i in range(0, width):
            for j in range(0, height):
                lcd_write(chigh)
                lcd_write(clow)

class Colors:
    BLACK   = 0x0000
    BLUE    = 0x001F
    RED     = 0xF800
    GREEN   = 0x07E0
    CYAN    = 0x07FF
    MAGENTA = 0xF81F
    YELLOW  = 0xFFE0
    WHITE   = 0xFFFF
    ORANGE  = 0xFE29
