from calcobjects.flexiblecodefield import FlexibleCodeField


class FlexibleCodeFields:
    # The init method or constructor
    def __init__(self, items):
        self.flexible_code_fields = []
        if isinstance(items, list):
            for item in items:
                self.flexible_code_fields.append(FlexibleCodeField(item))
        elif isinstance(items, dict):
            print("dict")
        else:
            print("unknown")

    def __str__(self):
        pretty_str = '/nFlexible Code Fields'
        for item in self.flexible_code_fields:
            pretty_str += '\n\t %s ' % item
        return pretty_str
