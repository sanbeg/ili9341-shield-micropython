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
        
    def _lcd_write(self, data:int):
        self._wr.off()
        self._emitter.emit(data)
        self._wr.on()

    def cmd_write(self, data:int):
        self._rs.off()
        self._lcd_write(data)
        
    def data_write(self, data:int):
        self._rs.on()
        self._lcd_write(data)
        
    def cmd_data(self, cmd, *data:int):
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
        for y in range(0, 38400 * 4): # 240*320/2
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
        
    @micropython.viper
    def draw_rect(self, col:int, row:int, width:int, height:int, color:int):
        self.cmd_data(0x2a, row >> 8, row & 0xFF, ((row+height-1) >> 8), ((row+height-1) & 0xFF))
        self.cmd_data(0x2b, col >> 8, col & 0xFF, ((col+width-1) >> 8), ((col+width-1) & 0xFF))
     
        lcd_write = self._lcd_write
        wr = self._wr
        emit = self._emitter.emit
        chigh = color >> 8
        clow = color & 0xFF

        self.cmd_data(0x2c)
        if clow == chigh:
            wr.off()
            emit(chigh)
            wr.on()
            wr.off()
            wr.on()
            for i in range(0, width * height - 1):
                wr.off()
                wr.on()
                wr.off()
                wr.on()
        else:
            for i in range(0, width * height):
                wr.off()
                emit(chigh)
                wr.on()
                wr.off()
                emit(clow)
                wr.on()

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

class FastColors:
    BLACK   = 0x0000
    BLUE    = 0x1818
    RED     = 0xE8E8
    GREEN   = 0x0707
    CYAN    = 0x5F5F
    MAGENTA = 0xB8B8
    YELLOW  = 0xE6E6
    WHITE   = 0xFFFF
    ORANGE  = 0xE2E2
    # addition
    DARK_GREEN  = 0x0404
    WHEAT       = 0xF6F6
    TURQUOISE   = 0x3737
    DARK_SLATE  = 0x2A2A
    LIME        = 0x4646
    INDIGO      = 0x5050
    STEEL       = 0x5D5D
    PURPLE      = 0x7070
    LIGHT_SLATE = 0x7474
    SKY         = 0x7E7E
    BRICK       = 0x8080
    BURLYWOOD   = 0x8B8B
    KHAKI       = 0xACAC
    GRAY        = 0xB5B5
    SLATE2      = 0xBEBE
    LIGHT_CYAN  = 0xDFDF
    THISTLE     = 0xFEFE
