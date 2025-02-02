"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        "Sets start point for SerialGenerator"
        self.start = start 
        self.current = start

    def generate(self):
        "Generates the next number when called"
        value = self.current
        self.current += 1
        return value

    def reset(self):
        "Resets the serial number to the start"
        self.current = self.start
