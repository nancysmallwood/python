# overrideType	required	TaxOverrideCode
# overrideReasonCode	optional	String (1 - 4)
from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str


class TaxOverride:
    # The init method or constructor
    def __init__(self, dic):
        self.override_type = None
        self.override_reason_code = None
        if dic is not None:
            self.override_type = get_dic_item(dic, get_attr_key(dic, 'overridetype'))
            self.override_reason_code = get_dic_item(dic, get_attr_key(dic, 'overridereasoncode'))

    def __str__(self):
        print_str = "override_type = %s, override_reason_code = %s" \
                    % (self.override_type, self.override_reason_code)
        return print_str

    def to_json(self):
        return '{"overrideType": %s, ' \
               '"overrideReasonCode": %s}' % \
               (coalesce_str(self.override_type),
                coalesce_str(self.override_reason_code))