class GenericParallelEmitter:
    "Emitter which uses generic Pin functions to emit parallel data"
    def __init__(self, d0, d1, d2, d3, d4, d5, d6, d7):
        self._pins = [d0, d1, d2, d3, d4, d5, d6, d7]
        
    def init(self):
        for pin in self._pins:
            pin.init(pin.OUT)

    @micropython.viper
    def emit(self, data:int):
        pins = self._pins
        d = int(data)

        pins[0].value((data >> 0) & 1)
        pins[1].value((data >> 1) & 1)
        pins[2].value((data >> 2) & 1)
        pins[3].value((data >> 3) & 1)
        pins[4].value((data >> 4) & 1)
        pins[5].value((data >> 5) & 1)
        pins[6].value((data >> 6) & 1)
        pins[7].value((data >> 7) & 1)
    