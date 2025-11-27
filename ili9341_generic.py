class GenericParallelEmitter:
    "Emitter which uses generic Pin functions to emit parallel data"
    def __init__(self, d0, d1, d2, d3, d4, d5, d6, d7):
        self._pins = [d0, d1, d2, d3, d4, d5, d6, d7]
        
    def init(self):
        for pin in self._pins:
            pin.init(pin.OUT)

    @staticmethod
    @micropython.viper
    def _emit_bit(data, pin, bit):
        boolean = (int(data) & (1<<int(bit))) > 0
        pin.value(boolean)
    
    def emit(self, data):
        emit_bit = self._emit_bit
        pins = self._pins
        d = int(data)
        emit_bit(d, pins[0], 0)
        emit_bit(d, pins[1], 1)
        emit_bit(d, pins[2], 2)
        emit_bit(d, pins[3], 3)
        emit_bit(d, pins[4], 4)
        emit_bit(d, pins[5], 5)
        emit_bit(d, pins[6], 6)
        emit_bit(d, pins[7], 7)
    