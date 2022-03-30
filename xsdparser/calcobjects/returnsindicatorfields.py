# ReturnsIndicatorField	0 - unlimited
from calcobjects.returnsindicatorfield import ReturnsIndicatorField


class ReturnsIndicatorFields:
    # The init method or constructor
    def __init__(self, items):
        self.returns_indicator_fields = []
        if isinstance(items, list):
            for item in items:
                self.returns_indicator_fields.append(ReturnsIndicatorField(item))
        elif isinstance(items, dict):
            print("dict")
        else:
            print("unknown")

    def __str__(self):
        pretty_str = ''
        for item in self.returns_indicator_fields:
            pretty_str += '\n %s ' % item
        return pretty_str
