import json

from soapparse import xml_to_dict, get_payload, get_quote, get_login, get_application_data

osp_path = '.\\media\\'
osp_file = 'real_sample.json'


class Osp:
    # The init method or constructor
    def __init__(self, json_str):
        self.timestamp = ''
        self.ecs_version = ''
        self.uuid = ''
        self.payload = ''
        self.message_type = ''
        self.version = ''
        self.company_code = ''
        self.agent_id = ''
        self.agent_version = ''
        self.agent_hostname = ''
        self.agent_ephemeral_id = ''
        self.agent_name = ''
        self.agent_type = ''
        self.log_file_path = ''
        self.log_offset = 0
        self.input_type = ''
        self.trusted_id = ''
        self.request_time = ''
        self.host_architecture = ''
        self.host_os_family = ''
        self.host_os_version = ''
        self.host_os_kernel = ''
        self.host_os_build = ''
        self.host_os_platform = ''
        self.host_os_name = ''
        self.host_id = ''
        self.host_hostname = ''
        self.host_ip = []
        self.host_mac = []
        self.host_name = ''
        self.cloud_account_id = ''
        self.cloud_region = ''
        self.cloud_instance_id = ''
        self.cloud_machine_type = ''
        self.cloud_provider = ''
        self.cloud_image_id = ''
        self.cloud_availability_zone = ''
        self.ip = ''
        self.host_dns = ''
        self.tags = []
        self.fields_doc_type = ''
        self.amazon_trace_id = ''
        self.login = None
        self.quote = None
        self.invoice = None
        self.tax_area_lookup = None
        self.application_data = None

        self.set_timestamp(json_str['@timestamp'])
        self.set_ecs(json_str['ecs'])
        self.set_uuid(json_str['uuid'])
        self.set_payload(json_str['payload'])
        self.set_message_type(json_str['messageType'])
        self.set_version(json_str['@version'])
        self.set_company_code(json_str['companyCode'])
        self.set_agent(json_str['agent'])
        self.set_log(json_str['log'])
        self.set_input(json_str['input'])
        self.set_trusted_id(json_str['trustedId'])
        self.set_request_time(json_str['requestTime'])
        self.set_host(json_str['host'])
        self.set_cloud(json_str['cloud'])
        self.set_ip(json_str['ip'])
        self.set_host_dns(json_str['hostDns'])
        self.set_tags(json_str['tags'])
        self.set_fields(json_str['fields'])
        self.set_amazon_trace_id(json_str['amazonTraceId'])

    def set_timestamp(self, timestamp):
        if timestamp is not None:
            self.timestamp = timestamp

    def set_ecs(self, ecs):
        if ecs is not None:
            if ecs['version'] is not None:
                self.ecs_version = ecs['version']

    def set_uuid(self, uuid):
        if uuid is not None:
            self.uuid = uuid

    def set_payload(self, payload):
        if payload is not None:
            self.payload = payload

    def set_message_type(self, message_type):
        if message_type is not None:
            self.message_type = message_type

    def set_version(self, version):
        if version is not None:
            self.version = version

    def set_company_code(self, company_code):
        if company_code is not None:
            self.company_code = company_code

    def set_agent(self, agent):
        if agent is not None:
            if agent['id'] is not None:
                self.agent_id = agent['id']
            if agent['version'] is not None:
                self.agent_version = agent['version']
            if agent['hostname'] is not None:
                self.agent_hostname = agent['hostname']
            if agent['ephemeral_id'] is not None:
                self.agent_ephemeral_id = agent['ephemeral_id']
            if agent['name'] is not None:
                self.agent_name = agent['name']
            if agent['type'] is not None:
                self.agent_type = agent['type']

    def set_log(self, log):
        if log is not None:
            if log['file'] is not None:
                if (log['file'])['path'] is not None:
                    self.log_file_path = (log['file'])['path']
            if log['offset'] is not None:
                self.log_offset = log['offset']

    def set_input(self, input_field):
        if input_field is not None:
            if input_field['type'] is not None:
                self.input_type = input_field['type']

    def set_trusted_id(self, trusted_id):
        if trusted_id is not None:
            self.trusted_id = trusted_id

    def set_request_time(self, request_time):
        if request_time is not None:
            self.request_time = request_time

    def set_host(self, host):
        if host is not None:
            if host['architecture'] is not None:
                self.host_architecture = host['architecture']
            if host['os'] is not None:
                if (host['os'])['family'] is not None:
                    self.host_os_family = (host['os'])['family']
                if (host['os'])['version'] is not None:
                    self.host_os_version = (host['os'])['version']
                if (host['os'])['kernel'] is not None:
                    self.host_os_kernel = (host['os'])['kernel']
                if (host['os'])['build'] is not None:
                    self.host_os_build = (host['os'])['build']
                if (host['os'])['platform'] is not None:
                    self.host_os_platform = (host['os'])['platform']
                if (host['os'])['name'] is not None:
                    self.host_os_name = (host['os'])['name']
            if host['id'] is not None:
                self.host_id = host['id']
            if host['hostname'] is not None:
                self.host_hostname = host['hostname']
            if host['ip'] is not None:
                self.host_ip = host['ip']
            if host['mac'] is not None:
                self.host_mac = host['mac']
            if host['name'] is not None:
                self.host_name = host['name']

    def set_cloud(self, cloud):
        if cloud is not None:
            if cloud['account'] is not None:
                if (cloud['account'])['id'] is not None:
                    self.cloud_account_id = (cloud['account'])['id']
            if cloud['region'] is not None:
                self.cloud_region = cloud['region']
            if cloud['instance'] is not None:
                if (cloud['instance'])['id'] is not None:
                    self.cloud_instance_id = (cloud['instance'])['id']
            if cloud['machine'] is not None:
                if (cloud['machine'])['type'] is not None:
                    self.cloud_machine_type = (cloud['machine'])['type']
            if cloud['provider'] is not None:
                self.cloud_provider = cloud['provider']
            if cloud['image'] is not None:
                if (cloud['image'])['id'] is not None:
                    self.cloud_image_id = (cloud['image'])['id']
            if cloud['availability_zone'] is not None:
                self.cloud_availability_zone = cloud['availability_zone']

    def set_ip(self, ip):
        if ip is not None:
            self.ip = ip

    def set_host_dns(self, host_dns):
        if host_dns is not None:
            self.host_dns = host_dns

    def set_tags(self, tags):
        if tags is not None:
            self.tags = tags

    def set_fields(self, fields):
        if fields is not None:
            if fields['doc_type'] is not None:
                self.fields_doc_type = fields['doc_type']

    def set_amazon_trace_id(self, amazon_trace_id):
        if amazon_trace_id is not None:
            self.amazon_trace_id = amazon_trace_id

    def __str__(self):
        print_str = "From str method of Osp: \ntimestamp is %s, \necs_version is %s, \nuuid = %s, \nmessage_type = %s, " \
                    "\nversion is %s, \ncompany_code = %s, \nagent_id = %s, \nagent_version = %s, " \
                    "\nagent_hostname = %s, \nagent_ephemeral_id is %s, \nagent_name is %s, \nagent_type is %s, " \
                    "\nlog_file_path is %s, \nlog_offset is %s, \ninput_type is %s, \ntrusted_id is %s, " \
                    "\nrequest_time is %s, \nhost_architecture is %s, \nhost_os_family is %s, \nhost_os_version is %s, " \
                    "\nhost_os_kernel is %s,\nhost_os_build is %s, \nhost_os_platform is %s, \nhost_os_name is %s, " \
                    "\nhost_id is %s, \nhost_hostname is %s, \nhost_ip is %s, \nhost_mac is %s, \nhost_name is %s, " \
                    "\ncloud_account_id is %s, \ncloud_region is %s, \ncloud_instance_id is %s, " \
                    "\ncloud_machine_type is %s, \ncloud_provider is %s, \ncloud_image_id is %s, " \
                    "\ncloud_availability_zone is %s, \nip is %s, \nhost_dns is %s, \ntags is %s," \
                    "\nfields_doc_type is %s, \namazon_trace_id is %s, \npayload is %s, " \
                    "\nlogin is %s, \nquote is %s, \napplication_data is %s" \
                    "" % (self.timestamp,
                          self.ecs_version,
                          self.uuid,
                          self.message_type,
                          self.version,
                          self.company_code,
                          self.agent_id,
                          self.agent_version,
                          self.agent_hostname,
                          self.agent_ephemeral_id,
                          self.agent_name,
                          self.agent_type,
                          self.log_file_path,
                          self.log_offset,
                          self.input_type,
                          self.trusted_id,
                          self.request_time,
                          self.host_architecture,
                          self.host_os_family,
                          self.host_os_version,
                          self.host_os_kernel,
                          self.host_os_build,
                          self.host_os_platform,
                          self.host_os_name,
                          self.host_id,
                          self.host_hostname,
                          self.host_ip,
                          self.host_mac,
                          self.host_name,
                          self.cloud_account_id,
                          self.cloud_region,
                          self.cloud_instance_id,
                          self.cloud_machine_type,
                          self.cloud_provider,
                          self.cloud_image_id,
                          self.cloud_availability_zone,
                          self.ip,
                          self.host_dns,
                          self.tags,
                          self.fields_doc_type,
                          self.amazon_trace_id,
                          self.payload,
                          self.login,
                          self.quote,
                          self.application_data)
        return print_str


# Read the Wide Tax Journal file into a string
# Returns:  string of JSON file contents
def read_json_file():
    with open(osp_path + osp_file, 'r') as file:
        data = file.read().replace('\n', '')
    return json.loads(data)


# MAIN -----------------------------------------------------------------
if __name__ == '__main__':
    # test1 = Osp(json.loads('{"@timestamp":"2021-02-09T21:59:01.951Z"}'))
    # print(test1.ztimestamp)
    json_str = read_json_file()
    test1 = Osp(json_str)
    print(test1)
    dictionary = xml_to_dict(test1.payload)
    if get_payload(dictionary) is not None:
        payload_dictionary = get_payload(dictionary)
        test1.login = get_login(payload_dictionary)
        test1.quote = get_quote(payload_dictionary)
        test1.application_data = get_application_data(payload_dictionary)

    # test2 = Osp(json.loads('{"@timestamp":"2021-02-09T21:59:01.951Z","ecs": {"version": "1.6.0"}}'))
    # print(test2.ecs_version)
