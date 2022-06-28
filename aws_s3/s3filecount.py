import boto3
import os

from awshvr.databaseutils import insert_s3_file, get_file_id, get_field_data_types, get_db_connection, \
    commit_and_close_db_connection, close_db_without_commit
from awshvr.wtjfile import get_s3_file_names_chunk, get_s3_gz_file_line_count, get_s3_total_file_count, \
    insert_s3_gz_file_contents, get_s3_folder_file_count

file_path = '.\\media\\'
file_name = '100-test.txt'



# MAIN -----------------------------------------------------------------
if __name__ == '__main__':
    #profile_name = "CST-Cloud-Production"
    profile_name = "ET-Sandbox"
    region_name = 'us-east-1'
    s3_bucket_name = 'et-vertexsmb-osplogs'
    #s3_folder_name = 'Request-Logs/Prod/Request-Logs/us-east-1/2022/01/31/'
    s3_folder_name = 'Response-Logs/Prod/Response-Logs/us-east-1/2022/01/31/'
    # s3_folder_name = "data_db/"
    # "wtj_1/","wtj_2/","wtj_3/","wtj_5/","wtj_4/"
    #s3_folders = ["data_db/wtj_1/tenantcode=1|Part0464724643020363/"]
    chunk_size = 1000

    # Using Custom Session (preferred)
    session = boto3.session.Session(profile_name=profile_name)

    # Using Resource Object
    aws_session_resource = session.resource(service_name='s3', region_name=region_name)
    s3_bucket = aws_session_resource.Bucket(s3_bucket_name)

    number_files = get_s3_folder_file_count(s3_bucket, s3_folder_name)
    print(number_files)
    # number_files_in_bucket = get_s3_total_file_count(s3_bucket)
    # print(number_files_in_bucket)

    # for folder in s3_folders:
    #     print(folder)
    #     number_files = get_s3_folder_file_count(s3_bucket, folder)
    #     print(number_files)
    #     files = get_s3_file_names_chunk(aws_session_resource, s3_bucket, folder, chunk_size)
    #     # Get all the file names
    #     for i in range(len(files)):
    #         print (files[i])
    #         # Split filename from full path
    #         for substr in files[i].split("/"):
    #             new_file_name = substr
    #             # name of folder starts with postingdate
    #             if "postingdate" in substr:
    #                 folder_name = substr
    #                 print(folder_name)
    #                 if not os.path.exists(substr):
    #                     os.makedirs(substr)
    #         print(new_file_name)
    #         new_file_path = folder_name + '/' + new_file_name
    #         print(new_file_path)
    #         try:
    #             s3_bucket.download_file(files[i], new_file_path)
    #         except botocore.exceptions.ClientError as e:
    #             if e.response['Error']['Code'] == "404":
    #                 print("The object does not exist.")
    #             else:
    #                 raise

    # Get a chunk of file names
    # files = get_s3_file_names_chunk(aws_session_resource, s3_bucket, s3_folder_name, chunk_size)

    # For each chunk of file names, get the number of rows
    # Remember, the first line in each WTJ file is the header row of field names
    # for i in range(len(files)):
    #     number_of_rows = get_s3_gz_file_line_count(aws_session_resource, s3_bucket_name, files[i]) - 1
    #     print (files[i])
    #     print (number_of_rows)
    #     insert_s3_file(files[i], number_of_rows)

    # # Get field types
    # conn = get_db_connection()
    # field_data_types = get_field_data_types(conn)
    # print('Fields and Datatypes loaded for file loading')
    # commit_and_close_db_connection(conn)
    #
    # # For file in the chunk, get the file contents and insert into database
    # for i in range(len(files)):
    #     conn = get_db_connection()
    #     if conn is not None:
    #         fileid = get_file_id(conn, files[i])
    #         if fileid is not None:
    #             return_code = insert_s3_gz_file_contents(conn, fileid, aws_session_resource, s3_bucket_name,
    #                                                      files[i], field_data_types)
    #             if return_code == 0:
    #                 commit_and_close_db_connection(conn)
    #             else:
    #                 close_db_without_commit(conn)
    #     print('File load complete for ' + files[i])


