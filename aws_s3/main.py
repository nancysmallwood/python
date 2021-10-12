import boto3

# Using Custom Session (preferred)
session = boto3.session.Session(profile_name="ET-Sandbox")

# Using Resource Object
s3 = session.resource(service_name='s3', region_name='us-east-1')

for bucket in s3.buckets.all():
    print(bucket)         # s3.Bucket(name='aws-athena-query-results-940542067323-us-east-1')
    print(bucket.name)    # aws-athena-query-results-940542067323-us-east-1

# Using Client Object which gives list in JSON
s3_client = session.client(service_name='s3', region_name='us-east-1')

# Literally All information
print(s3_client.list_buckets())   # {'ResponseMetadata': {'RequestId': 'HSZ9DKGYH4ZK9VE5.....

# Just the buckets
print(s3_client.list_buckets().get('Buckets'))  # [{'Name': 'aws-athena-query-results-94054206 ....

# One by one
for bucket_info in s3_client.list_buckets().get('Buckets'):
    print(bucket_info.get('Name'))    # aws-athena-query-results-940542067323-us-east-1
    if bucket_info.get('Name') == 'emergent-tech-telemetry-data-stage':
        print('GOT IT')