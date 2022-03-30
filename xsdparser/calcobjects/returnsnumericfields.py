# ReturnsNumericField	0 - unlimited
from calcobjects.returnsnumericfield import ReturnsNumericField


class ReturnsNumericFields:
    # The init method or constructor
    def __init__(self, items):
        self.returns_numeric_fields = []
        if isinstance(items, list):
            for item in items:
                self.returns_numeric_fields.append(ReturnsNumericField(item))
        elif isinstance(items, dict):
            print("dict")
        else:
            print("unknown")

    def __str__(self):
        pretty_str = ''
        for item in self.returns_numeric_fields:
            pretty_str += '\n %s ' % item
        return pretty_str
