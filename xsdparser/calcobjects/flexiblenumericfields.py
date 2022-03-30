from calcobjects.flexiblenumericfield import FlexibleNumericField


class FlexibleNumericFields:
    # The init method or constructor
    def __init__(self, items):
        self.flexible_numeric_fields = []
        if isinstance(items, list):
            for item in items:
                self.flexible_numeric_fields.append(FlexibleNumericField(item))
        elif isinstance(items, dict):
            print("dict")
        else:
            print("unknown")

    def __str__(self):
        pretty_str = '/nFlexible Numeric Fields'
        for item in self.flexible_numeric_fields:
            pretty_str += '\n\t %s ' % item
        return pretty_str
