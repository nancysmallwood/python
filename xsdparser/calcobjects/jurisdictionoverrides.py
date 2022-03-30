from calcobjects.jurisdictionoverride import JurisdictionOverride


class JurisdictionOverrides:
    # The init method or constructor
    def __init__(self, items):
        self.jurisdiction_overrides = []
        if isinstance(items, list):
            for item in items:
                self.jurisdiction_overrides.append(JurisdictionOverride(item))
        elif isinstance(items, dict):
            print("dict")
        else:
            print("unknown")

    def __str__(self):
        pretty_str = ''
        for item in self.jurisdiction_overrides:
            pretty_str += '\n %s ' % item
        return pretty_str
