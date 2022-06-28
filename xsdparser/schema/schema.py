# Header and footer of every request/response
from pyspark.sql.types import StructType, StringType, LongType, DoubleType, ArrayType, StructField, BooleanType

# Custom addition for traceability back to the source OSP Log
osp_source_schema = StructType([
    StructField('file', StringType(), True),
    StructField('row', LongType(), True),
    StructField('messageType', StringType(), True)
])

log_schema = StructType([
    StructField('file',
                StructType([
                    StructField('path', StringType(), True)])),
    StructField('offset', LongType(), True)])

agent_schema= StructType([
    StructField('type', StringType(), True),
    StructField('id', StringType(), True),
    StructField('hostname', StringType(), True),
    StructField('ephemeral_id', StringType(), True),
    StructField('version', StringType(), True),
    StructField('name', StringType(), True)
])

host_schema = StructType([
    StructField("os",
                StructType([
                    StructField('name', StringType(), True),
                    StructField('platform', StringType(), True),
                    StructField('kernel', StringType(), True),
                    StructField('version', StringType(), True),
                    StructField('build', StringType(), True),
                    StructField('family', StringType(), True)])),
    StructField('id', StringType(), True),
    StructField('hostname', StringType(), True),
    StructField('mac',ArrayType(StringType()),True),
    StructField('ip',ArrayType(StringType()),True),
    StructField('architecture',StringType(),True),
    StructField('name',StringType(),True)])

input_schema = StructType([
    StructField('type', StringType(), True)])

fields_schema = StructType([
    StructField('doc_type', StringType(), True)])

cloud_schema = StructType([
    StructField("account",
                StructType([
                    StructField('id', StringType(), True)])),
    StructField("instance",
                StructType([
                StructField('id', StringType(), True)])),
    StructField("image",
                StructType([
                StructField('id', StringType(), True)])),
    StructField("machine",
                StructType([
                StructField('type', StringType(), True)])),
    StructField('availability_zone', StringType(), True),
    StructField('region', StringType(), True),
    StructField('provider', StringType(), True)])

ecs_schema = StructType([
    StructField('version', StringType(), True)])

# Payload "Login" and "Application Data" sections
login_schema = StructType([
    StructField('trusted_id', StringType(), True),
    StructField('user_name', StringType(), True)
])

application_property_schema = StructType([
    StructField('application_property', StringType(), True),
    StructField('key', StringType(), True)
])

application_properties_schema = StructType([
    StructField('application_properties', ArrayType(StructType(application_property_schema)))
])

log_entry_schema = StructType([
    StructField('log_level', StringType(), True),
    StructField('instance_id', StringType(), True),
    StructField('thread_id', StringType(), True),
    StructField('class_name', StringType(), True),
    StructField('exception', StringType(), True)
])

log_entries_schema =StructType([
    StructField('log_entries',ArrayType(StructType(log_entry_schema)))
])

applicationdata_schema = StructType([
    StructField('sender', StringType(), True),
    StructField('response_time_ms', StringType(), True),
    StructField('application_properties',StructType(application_properties_schema)),
    StructField('log_entries',StructType(log_entries_schema))
])

# Tax Data Components
# Postal Address, Currency, etc.
# Sub-Components used to construct the Line Item and Message

postal_address_schema = StructType([
    StructField('street_address_1', StringType(), True),
    StructField('street_address_2', StringType(), True),
    StructField('city', StringType(), True),
    StructField('main_division', StringType(), True),
    StructField('sub_division', StringType(), True),
    StructField('postal_code', StringType(), True),
    StructField('country', StringType(), True)
])

currency_schema = StructType([
    StructField('iso_currency_name', StringType(), True),
    StructField('iso_currency_code_alpha', StringType(), True),
    StructField('iso_currency_code_num', StringType(), True)
])

currency_conversion_schema = StructType([
    StructField('currency_conversion', DoubleType(), True),
    StructField('currency',StructType(currency_schema))
])

location_schema = StructType([
    StructField('currency_conversion',StructType(currency_conversion_schema)),
    StructField('tax_area_id', StringType(), True),
    StructField('latitude', StringType(), True),
    StructField('longitude', StringType(), True),
    StructField('location_customs_status', StringType(), True),
    StructField('location_code', StringType(), True),
    StructField('external_jurisdiction_code', StringType(), True),
    StructField('postal_address',StructType(postal_address_schema))
])

imposition_type_schema = StructType([
    StructField('imposition_type', StringType(), True),
    StructField('user_defined', BooleanType(), True),
    StructField('imposition_type_id', StringType(), True),
    StructField('withholding_type', StringType(), True)
])

seller_schema = StructType([
    StructField('company', StringType(), True),
    StructField('physical_origin',StructType(location_schema))
])

customer_code_schema = StructType([
    StructField('customer_code', StringType(), True),
    StructField('class_code', StringType(), True),
    StructField('is_business_indicator', BooleanType(), True)
])

customer_schema = StructType([
    StructField('destination', StructType(location_schema)),
    StructField('customer_code',StructType(customer_code_schema))
])

product_schema = StructType([
    StructField('product', StringType(), True),
    StructField('product_class', StringType(), True)
])

quantity_schema = StructType([
    StructField('quantity', StringType(), True),
    StructField('unit_of_measure', StringType(), True)
])

# Tax Components

jurisdiction_schema = StructType([
    StructField('jurisdictionlevel', StringType(), True),
    StructField('jurisdictionid', StringType(), True),
    StructField('effectivedate', StringType(), True),
    StructField('expirationdate', StringType(), True),
    StructField('externaljurisdictioncode', StringType(), True)
])

tax_exempt_schema = StructType([
    StructField('amount', StringType(), True),
    StructField('unit_of_measure', StringType(), True)
])

tax_imposition_schema = StructType([
    StructField('imposition', StringType(), True),
    StructField('user_defined', BooleanType(), True),
    StructField('imposition_id', StringType(), True)
])

tax_rule_schema = StructType([
    StructField('tax_rule_id', StringType(), True),
    StructField('user_defined', BooleanType(), True),
    StructField('sales_tax_holiday_indicator', BooleanType(), True),
    StructField('tax_rule_type', StringType(), True)
])

tax_schema = StructType([
    StructField('taxresult', StringType(), True),
    StructField('taxtype', StringType(), True),
    StructField('situs', StringType(), True),
    StructField('maxtaxindicator', BooleanType(), True),
    StructField('notregisteredindicator', BooleanType(), True),
    StructField('inputoutputtype', StringType(), True),
    StructField('taxcode', StringType(), True),
    StructField('vertextaxcode', StringType(), True),
    StructField('reasoncode', StringType(), True),
    StructField('filingcategorycode', StringType(), True),
    StructField('isservice', BooleanType(), True),
    StructField('rateclassification', StringType(), True),
    StructField('taxcollectedfromparty', StringType(), True),
    StructField('taxstructure', StringType(), True),
    StructField('jurisdiction',StructType(jurisdiction_schema)),
    StructField('calculated_tax', StringType(), True),
    StructField('effective_rate', StringType(), True),
    StructField('tax_apportionment_rate', StringType(), True),
    StructField('basis_reduction_percentage', StringType(), True),
    StructField('exempt',StructType(tax_exempt_schema)),
    StructField('nontaxable',StructType(tax_exempt_schema)),
    StructField('taxable',StructType(tax_exempt_schema)),
    StructField('reporting_basis', StringType(), True),
    StructField('imposition',StructType(tax_imposition_schema)),
    StructField('imposition_type',StructType(imposition_type_schema)),
    StructField('tax_rule_id',StructType(tax_rule_schema)),
    StructField('basis_rule_id',StructType(tax_rule_schema)),
    StructField('inclusion_rule_id',StructType(tax_rule_schema)),
    StructField('max_tax_rule_id',StructType(tax_rule_schema)),
    StructField('recoverable_rule_id',StructType(tax_rule_schema)),
    StructField('post_calculation_evaluation_rule_id',StructType(tax_rule_schema)),
    StructField('credit_rule_id',StructType(tax_rule_schema)),
    StructField('basis_apportionment_rule_id',StructType(tax_rule_schema)),
    StructField('tax_rate_adjustment_rule_id',StructType(tax_rule_schema)),
    StructField('tax_apportionment_rule_id',StructType(tax_rule_schema)),
    StructField('accumulation_rule_id',StructType(tax_rule_schema)),
    StructField('telecom_unit_conversion_rule_id',StructType(tax_rule_schema)),
    StructField('reporting_basis_rule_id',StructType(tax_rule_schema)),
    StructField('recoverable_amount', StringType(), True),
    StructField('recoverable_percent', StringType(), True),
    StructField('blocking_recoverable_percent', StringType(), True),
    StructField('partial_exempt_recoverable_percent', StringType(), True),
    StructField('unrecoverable_amount', StringType(), True),
    StructField('original_tax', StringType(), True),
    StructField('included_tax', StringType(), True),
    StructField('nominal_rate', StringType(), True),
    StructField('markup_rate', StringType(), True)
])

taxes_schema = StructType([
    StructField('tax_items', ArrayType(StructType(tax_schema)))
])

# Line Item and Message Components

line_item_schema = StructType([
    StructField('line_item_number', StringType(), True),
    StructField('line_item_id', StringType(), True),
    StructField('fair_market_value', StringType(), True),
    StructField('unit_price', StringType(), True),
    StructField('extended_price', StringType(), True),
    StructField('total_tax', StringType(), True),
    StructField('product',StructType(product_schema)),
    StructField('quantity',StructType(quantity_schema)),
    StructField('seller',StructType(seller_schema)),
    StructField('customer',StructType(customer_schema)),
    StructField('taxes',StructType(taxes_schema))
])

line_items_schema = StructType([
    StructField('line_items', ArrayType(StructType(line_item_schema)))
])

# Payload Message
message_schema = StructType([
    StructField('return_assisted_parameters_indicator', BooleanType(), True),
    StructField('return_generated_line_items_indicator', BooleanType(), True),
    StructField('round_at_line_level', BooleanType(), True),
    StructField('subtotal', StringType(), True),
    StructField('total', StringType(), True),
    StructField('totaltax', StringType(), True),
    StructField('company_code_currency',StructType(currency_schema)),
    StructField('original_currency',StructType(currency_schema)),
    StructField('currency',StructType(currency_schema)),
    StructField('document_number', StringType(), True),
    StructField('document_date', StringType(), True),
    StructField('posting_date', StringType(), True),
    StructField('transaction_type', StringType(), True),
    StructField('line_items',StructType(line_items_schema))
])


# Payload
payload_schema = StructType([
    StructField("login",StructType(login_schema)),
    StructField("application_data",StructType(applicationdata_schema)),
    StructField('message_type', StringType(), True),
    StructField("message",StructType(message_schema))])


# Complete OSP Log Item
osplogitem_schema = StructType([
    StructField('ospSource', StructType(osp_source_schema), True),
    StructField('hostDns', StringType(), True),
    StructField('@timestamp', StringType(), True),
    StructField("log",StructType(log_schema)),
    StructField('trustedId', StringType(), True),
    StructField('companyCode', StringType(), True),
    StructField('messageType', StringType(), True),
    StructField('payloadType', StringType(), True),
    StructField("agent",StructType(agent_schema)),
    StructField('requestTime', StringType(), True),
    StructField('responseTime', StringType(), True),
    StructField('uuid', StringType(), True),
    StructField("host",StructType(host_schema)),
    StructField("input",StructType(input_schema)),
    StructField("tags",ArrayType(StringType())),
    StructField('podId', StringType(), True),
    StructField("fields",StructType(fields_schema)),
    StructField("cloud",StructType(cloud_schema)),
    StructField('@version', StringType(), True),
    StructField("payload",StructType(payload_schema)),
    StructField("ecs",StructType(ecs_schema)),
    StructField('amazonTraceId', StringType(), True)
])