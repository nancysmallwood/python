from calcobjects.overrideloggingthreshold import OverrideLoggingThreshold


class OverrideLoggingThresholds:
    # The init method or constructor
    def __init__(self, items):
        self.override_logging_thresholds = [OverrideLoggingThreshold(None)]
        if items is not None:
            if isinstance(items, list):
                for item in items:
                    self.override_logging_thresholds.append(OverrideLoggingThreshold(item))
            elif isinstance(items, dict):
                self.override_logging_thresholds.append(OverrideLoggingThreshold(items))

    def __str__(self):
        pretty_str = ''
        for item in self.override_logging_thresholds:
            pretty_str += '\n %s ' % item
        return pretty_str

    def to_json(self):
        json_str = '['
        number_override_logging_thresholds = len(self.override_logging_thresholds)
        counter = 0
        for item in self.override_logging_thresholds:
            counter += 1
            json_str += item.to_json()
            if counter != number_override_logging_thresholds:
                json_str += ','
        json_str += ']'
        return json_str
