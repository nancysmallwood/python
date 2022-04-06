# OverrideLoggingThreshold	0 - unlimited
# thresholdScope	optional

from util.dictionary_util import get_attr_key, get_dic_item, null, coalesce_str


class OverrideLoggingThreshold:
    # The init method or constructor
    def __init__(self, dic):
        self.override_logging_threshold = None
        self.threshold_scope = None
        if dic is not None:
            self.override_logging_threshold = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.threshold_scope = get_dic_item(dic, get_attr_key(dic, 'thresholdscope'))

    def __str__(self):
        print_str = "override_logging_threshold=%s, threshold_scope= %s" % \
                    (self.override_logging_threshold, self.threshold_scope)
        return print_str

    def to_json(self):
        return '{"OverrideLoggingThreshold": %s, ' \
               '"thresholdScope": %s}' % \
               (coalesce_str(self.override_logging_threshold),
                coalesce_str(self.threshold_scope))
