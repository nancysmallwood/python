# MessageLogging	0 - 1
# returnLogEntries	optional	Boolean
# OverrideLoggingThreshold	0 - unlimited
from calcobjects.overrideloggingthreshold import OverrideLoggingThreshold
from calcobjects.util import get_attr_key, get_dic_item, get_dic_key


class MessageLogging:
    # The init method or constructor
    def __init__(self, dic):
        # Objects
        if get_dic_key(dic, 'overrideloggingthreshold') is not None:
            self.override_logging_threshold = \
                OverrideLoggingThreshold(get_dic_item(dic, get_dic_key(dic, 'overrideloggingthreshold')))
        else:
            self.override_logging_threshold = None
        # Fields
        self.message_logging = get_dic_item(dic, get_attr_key(dic, 'text'))
        self.return_log_entries = get_dic_item(dic, get_attr_key(dic, 'returnlogentries'))

    def __str__(self):
        print_str = "override_logging_threshold=%s, message_logging= %s, return_log_entries= %s" % \
                    (self.override_logging_threshold, self.message_logging, self.return_log_entries)
        return print_str

