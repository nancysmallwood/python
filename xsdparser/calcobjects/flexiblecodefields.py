from calcobjects.flexiblecodefield import FlexibleCodeField


class FlexibleCodeFields:
    # The init method or constructor
    def __init__(self, items):
        self.flexible_code_fields = [FlexibleCodeField(None)]
        if items is not None:
            if isinstance(items, list):
                for item in items:
                    self.flexible_code_fields.append(FlexibleCodeField(item))
            elif isinstance(items, dict):
                self.flexible_code_fields.append(FlexibleCodeField(items))

    def __str__(self):
        pretty_str = '/nFlexible Code Fields'
        for item in self.flexible_code_fields:
            pretty_str += '\n\t %s ' % item
        return pretty_str

    def to_json(self):
        json_str = '['
        number_flexible_code_fields = len(self.flexible_code_fields)
        counter = 0
        for item in self.flexible_code_fields:
            counter += 1
            json_str += item.to_json()
            if counter != number_flexible_code_fields:
                json_str += ','
        json_str += ']'
        return json_str
