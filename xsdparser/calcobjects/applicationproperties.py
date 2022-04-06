# ApplicationProperty	0 - unlimited
from calcobjects.applicationproperty import ApplicationProperty
from util.dictionary_util import coalesce_str


class ApplicationProperties:
    # The init method or constructor
    def __init__(self, items):
        self.application_properties = [ApplicationProperty(None)]
        if items is not None:
            if isinstance(items, list):
                for item in items:
                    self.application_properties.append(ApplicationProperty(item))
            elif isinstance(items, dict):
                self.application_properties.append(ApplicationProperty(items))

    def __str__(self):
        pretty_str = ''
        for item in self.application_properties:
            pretty_str += '\n %s ' % item
        return pretty_str

    def to_json(self):
        json_str = '['
        number_application_properties = len(self.application_properties)
        counter = 0
        for item in self.application_properties:
            counter += 1
            json_str += item.to_json()
            if counter != number_application_properties:
                json_str += ','
        json_str += ']'
        return json_str
