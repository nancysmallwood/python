# MessageLogging	0 - 1
# returnLogEntries	optional	Boolean
# OverrideLoggingThreshold	0 - unlimited
from calcobjects.overrideloggingthresholds import OverrideLoggingThresholds
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key, null, coalesce_str


class MessageLogging:
    # The init method or constructor
    def __init__(self, dic):
        self.override_logging_thresholds = OverrideLoggingThresholds(dic)
        self.message_logging = None
        self.return_log_entries = False
        if dic is not None:
            # Objects
            if get_dic_key(dic, 'overrideloggingthreshold') is not None:
                self.override_logging_thresholds = \
                    OverrideLoggingThresholds(get_dic_item(dic, get_dic_key(dic, 'overrideloggingthreshold')))
            # Fields
            self.message_logging = get_dic_item(dic, get_attr_key(dic, 'text'))
            if get_dic_item(dic, get_attr_key(dic, 'returnlogentries')) is not None:
                self.return_log_entries = get_dic_item(dic, get_attr_key(dic, 'returnlogentries'))

    def __str__(self):
        print_str = "override_logging_threshold=%s, message_logging= %s, return_log_entries= %s" % \
                    (self.override_logging_thresholds, self.message_logging, self.return_log_entries)
        return print_str

    def to_json(self):
        return '{"MessageLogging": %s, ' \
               '"returnLogEntries": %s, ' \
               '"OverrideLoggingThreshold": %s}' % \
               (coalesce_str(self.message_logging),
                coalesce_str(self.return_log_entries),
                self.override_logging_thresholds.to_json())

