# LogEntry	0 - unlimited

from calcobjects.logentry import LogEntry


class LogEntries:
    # The init method or constructor
    def __init__(self, items):
        self.log_entries = [LogEntry(None)]
        if items is not None:
            if isinstance(items, list):
                for item in items:
                    self.log_entries.append(LogEntry(item))
            elif isinstance(items, dict):
                self.log_entries.append(LogEntry(items))

    def __str__(self):
        pretty_str = ''
        for item in self.log_entries:
            pretty_str += '\n %s ' % item
        return pretty_str

    def to_json(self):
        json_str = '['
        number_log_entries = len(self.log_entries)
        counter = 0
        for item in self.log_entries:
            counter += 1
            json_str += item.to_json()
            if counter != number_log_entries:
                json_str += ','
        json_str += ']'
        return json_str

