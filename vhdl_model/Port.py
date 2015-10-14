from Signal import Signal
from enum import Enum


class Direction(Enum):
    IN = 1,
    OUT = 2,
    INOUT = 3,
    BUFFER = 4,
    LINKAGE = 5


class Port:

    def __init__(self, internal_signal, external_signal, direction):
        self.internal_signal = internal_signal
        self.external_signal = external_signal
        self.direction = direction
