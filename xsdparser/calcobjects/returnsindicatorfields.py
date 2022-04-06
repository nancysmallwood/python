# ReturnsIndicatorField	0 - unlimited
from calcobjects.returnsindicatorfield import ReturnsIndicatorField


class ReturnsIndicatorFields:
    # The init method or constructor
    def __init__(self, items):
        self.returns_indicator_fields = [ReturnsIndicatorField(None)]
        if items is not None:
            if isinstance(items, list):
                for item in items:
                    self.returns_indicator_fields.append(ReturnsIndicatorField(item))
            elif isinstance(items, dict):
                self.returns_indicator_fields.append(ReturnsIndicatorField(items))

    def __str__(self):
        pretty_str = ''
        for item in self.returns_indicator_fields:
            pretty_str += '\n %s ' % item
        return pretty_str

    def to_json(self):
        json_str = '['
        number_returns_indicator_fields = len(self.returns_indicator_fields)
        counter = 0
        for item in self.returns_indicator_fields:
            counter += 1
            json_str += item.to_json()
            if counter != number_returns_indicator_fields:
                json_str += ','
        json_str += ']'
        return json_str
