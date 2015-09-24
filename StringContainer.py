from enum import Enum


class StringContainerCategory(Enum):
    Name = 1,
    Label = 2,
    Instantiated_Unit = 3


class StringContainer:

    def __init__(self, category):
        self.type = category
        self.value = ""

    def set_identifier(self, value):
        if self.value == "":
            self.value += "_"
        self.value += value
