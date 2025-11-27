class GenericParallelEmitter:
    "Emitter which uses generic Pin functions to emit parallel data"
    def __init__(self, d0, d1, d2, d3, d4, d5, d6, d7):
        self.pins = [d0, d1, d2, d3, d4, d5, d6, d7]
        
    def init(self):
        for pin in self.pins:
            pin.init(pin.OUT)

    @staticmethod
    def _emit_bit(data, pin, bit):
        boolean = (data & (1<<bit)) > 0
        pin.value(boolean)
    
    def emit(data):
        for bit, pin in self.pins:
            _emit_bit(data, pin, bit)
            
    