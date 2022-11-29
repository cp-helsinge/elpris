import machine
import time


class RelayControl(object):
    def __init__(self):
        self.relay_pins = [27, 32, 25, 33]
        self.pin = []

        for pin_num in range(4):
            self.pin.append(machine.Pin(self.relay_pins[pin_num], machine.Pin.OUT))

    def on(self, relay: int):
        self.pin[relay].value(0)

    def off(self, relay: int):
        self.pin[relay].value(1)

    def all_on(self, delay: float = .5):
        for pn in range(4):
            self.on(relay=pn)
            time.sleep(delay)

    def all_off(self, delay: float = .5):
        for pn in range(4):
            self.off(relay=pn)
            time.sleep(delay)


if __name__ == '__main__':
    relay = RelayControl()
    while True:
        relay.all_on()
        time.sleep(2)
        relay.all_off()
        time.sleep(2)

# eof
