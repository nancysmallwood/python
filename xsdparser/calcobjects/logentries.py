# LogEntry	0 - unlimited

from calcobjects.logentry import LogEntry


class LogEntries:
    # The init method or constructor
    def __init__(self, items):
        self.log_entries = []
        if isinstance(items, list):
            for item in items:
                self.log_entries.append(LogEntry(item))
        elif isinstance(items, dict):
            print("dict")
        else:
            print("unknown")

    def __str__(self):
        pretty_str = ''
        for item in self.log_entries:
            pretty_str += '\n %s ' % item
        return pretty_str
