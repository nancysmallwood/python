from calcobjects.jurisdictionoverride import JurisdictionOverride


class JurisdictionOverrides:
    # The init method or constructor
    def __init__(self, items):
        self.jurisdiction_overrides = [JurisdictionOverride(None)]
        if items is not None:
            if isinstance(items, list):
                for item in items:
                    self.jurisdiction_overrides.append(JurisdictionOverride(item))
            elif isinstance(items, dict):
                self.jurisdiction_overrides.append(JurisdictionOverride(items))

    def __str__(self):
        pretty_str = ''
        for item in self.jurisdiction_overrides:
            pretty_str += '\n %s ' % item
        return pretty_str

    def to_json(self):
        json_str = '['
        number_jurisdiction_overrides = len(self.jurisdiction_overrides)
        counter = 0
        for item in self.jurisdiction_overrides:
            counter += 1
            json_str += item.to_json()
            if counter != number_jurisdiction_overrides:
                json_str += ','
        json_str += ']'
        return json_str