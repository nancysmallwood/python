import boto3
import gzip

file_path = '.\\media\\'
file_name = 'allwtjfiles-pod1.txt'
# file_name = 'test.txt'

# Using Custom Session (preferred)
# session = boto3.session.Session(profile_name="ET-Sandbox")
session = boto3.session.Session(profile_name="CST-Cloud-Production")

# Using Resource Object
s3 = session.resource(service_name='s3', region_name='us-east-1')

# for bucket in s3.buckets.all():
#     print(bucket)         # s3.Bucket(name='aws-athena-query-results-940542067323-us-east-1')
#     print(bucket.name)    # aws-athena-query-results-940542067323-us-east-1

# Using Client Object which gives list in JSON
s3_client = session.client(service_name='s3', region_name='us-east-1')

# Literally All information
# print(s3_client.list_buckets())   # {'ResponseMetadata': {'RequestId': 'HSZ9DKGYH4ZK9VE5.....

# Just the buckets
# print(s3_client.list_buckets().get('Buckets'))  # [{'Name': 'aws-athena-query-results-94054206 ....

# One by one
# for bucket_info in s3_client.list_buckets().get('Buckets'):
#     print(bucket_info.get('Name'))    # aws-athena-query-results-940542067323-us-east-1
#     if bucket_info.get('Name') == 'emergent-tech-telemetry-data-stage':
#         print('GOT IT')

my_bucket = s3.Bucket('vertexsmb-hvr-prod')
file_counter = 0
total_lines = 0

with open(file_path + file_name, 'w') as txtfile:

    for object_summary in my_bucket.objects.filter(Prefix="archive/1/"):
        # obj = s3.Object('vertexsmb-hvr-prod', object_summary.key)
        txtfile.write(object_summary.key)
        txtfile.write('\n')

        # with gzip.GzipFile(fileobj=obj.get()["Body"]) as gzipfile:
        #     content = gzipfile.read()
        #     lines = content.decode('utf8').count('\n')
        #     total_lines += lines
        #     txtfile.write(object_summary.key)
        #     txtfile.write(", ")
        #     txtfile.write(str(lines))
        #     txtfile.write('\n')

        file_counter += 1
        # if file_counter == 5:
        #     break
        if (file_counter % 1000) == 0:
            print(file_counter)

    # txtfile.write('Total lines: ')
    # txtfile.write(str(total_lines))
    # txtfile.write('\n')

