from calcobjects.tax import Tax


class Taxes:
    # The init method or constructor
    def __init__(self, items):
        self.tax_items = [Tax(None)]
        if items is not None:
            if isinstance(items, list):
                for item in items:
                    self.tax_items.append(Tax(item))
            elif isinstance(items, dict):
                self.tax_items.append(Tax(items))