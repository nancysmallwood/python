# ReturnsCodeField	0 - unlimited
from calcobjects.returnscodefield import ReturnsCodeField


class ReturnsCodeFields:
    # The init method or constructor
    def __init__(self, items):
        self.returns_code_fields = [ReturnsCodeField(None)]
        if items is not None:
            if isinstance(items, list):
                for item in items:
                    self.returns_code_fields.append(ReturnsCodeField(item))
            elif isinstance(items, dict):
                self.returns_code_fields.append(ReturnsCodeField(items))

    def __str__(self):
        pretty_str = ''
        for item in self.returns_code_fields:
            pretty_str += '\n %s ' % item
        return pretty_str

    def to_json(self):
        json_str = '['
        number_returns_code_fields = len(self.returns_code_fields)
        counter = 0
        for item in self.returns_code_fields:
            counter += 1
            json_str += item.to_json()
            if counter != number_returns_code_fields:
                json_str += ','
        json_str += ']'
        return json_str
