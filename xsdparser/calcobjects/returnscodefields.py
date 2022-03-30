# ReturnsCodeField	0 - unlimited
from calcobjects.returnscodefield import ReturnsCodeField


class ReturnsCodeFields:
    # The init method or constructor
    def __init__(self, items):
        self.returns_code_fields = []
        if isinstance(items, list):
            for item in items:
                self.returns_code_fields.append(ReturnsCodeField(item))
        elif isinstance(items, dict):
            print("dict")
        else:
            print("unknown")

    def __str__(self):
        pretty_str = ''
        for item in self.returns_code_fields:
            pretty_str += '\n %s ' % item
        return pretty_str
