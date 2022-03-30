# ApplicationProperty	0 - unlimited
from calcobjects.applicationproperty import ApplicationProperty


class ApplicationProperties:
    # The init method or constructor
    def __init__(self, items):
        self.application_properties = []
        if isinstance(items, list):
            for item in items:
                self.application_properties.append(ApplicationProperty(item))
        elif isinstance(items, dict):
            print("dict")
        else:
            print("unknown")

    def __str__(self):
        pretty_str = ''
        for item in self.application_properties:
            pretty_str += '\n %s ' % item
        return pretty_str