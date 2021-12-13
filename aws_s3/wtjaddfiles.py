import boto3

from awshvr.databaseutils import insert_s3_file, get_file_id, get_field_data_types, get_db_connection, \
    commit_and_close_db_connection, close_db_without_commit
from awshvr.wtjfile import get_s3_file_names_chunk, get_s3_gz_file_line_count, get_s3_total_file_count, \
    insert_s3_gz_file_contents

file_path = '.\\media\\'
file_name = '100-test.txt'

# MAIN -----------------------------------------------------------------
if __name__ == '__main__':
    profile_name = "CST-Cloud-Production"
    region_name = 'us-east-1'
    s3_bucket_name = 'vertexsmb-hvr-prod'
    s3_folder_name = "archive/1/"
    chunk_size = 100

    # Using Custom Session (preferred)
    session = boto3.session.Session(profile_name=profile_name)

    # Using Resource Object
    aws_session_resource = session.resource(service_name='s3', region_name=region_name)

    s3_bucket = aws_session_resource.Bucket(s3_bucket_name)

    # number_files_in_bucket = get_s3_total_file_count(s3_bucket)
    # print(number_files_in_bucket)

    # Get a chunk of file names
    files = get_s3_file_names_chunk(aws_session_resource, s3_bucket, s3_folder_name, chunk_size)

    if files is not None:
        # For each chunk of file names, get the number of rows
        # Remember, the first line in each WTJ file is the header row of field names
        for i in range(len(files)):
            number_of_rows = get_s3_gz_file_line_count(aws_session_resource, s3_bucket_name, files[i]) - 1
            print (files[i])
            print (number_of_rows)
            insert_s3_file(files[i], number_of_rows)

