from calcobjects.flexibledatefield import FlexibleDateField


class FlexibleDateFields:
    # The init method or constructor
    def __init__(self, items):
        self.flexible_date_fields = []
        if isinstance(items, list):
            for item in items:
                self.flexible_date_fields.append(FlexibleDateField(item))
        elif isinstance(items, dict):
            print("dict")
        else:
            print("unknown")

    def __str__(self):
        pretty_str = '/nFlexible Date Fields'
        for item in self.flexible_date_fields:
            pretty_str += '\n\t %s ' % item
        return pretty_str
