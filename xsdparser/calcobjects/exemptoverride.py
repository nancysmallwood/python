# ExemptOverride	0 - 1 text 0 - 1	number amount
# overrideExemptReasonCode	optional	String (1 - 4)

from calcobjects.util import get_attr_key, get_dic_item


class ExemptOverride:
    # The init method or constructor
    def __init__(self, dic):
        self.exempt_override = get_dic_item(dic, get_attr_key(dic, 'text'))
        self.override_exempt_reason_code = get_dic_item(dic, get_attr_key(dic, 'overrideexemptreasoncode'))

    def __str__(self):
        print_str = "exempt_override=%s, override_exempt_reason_code= %s" % \
                    (self.exempt_override, self.override_exempt_reason_code)
        return print_str
