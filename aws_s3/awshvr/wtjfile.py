import gzip


# Get a chunk of file names, returns an array
from io import TextIOWrapper

from awshvr.databaseutils import insert_wtj_row


def get_s3_file_names_chunk(aws_session_resource, s3_bucket, s3_folder, chunk_size):
    file_counter = 0
    file_name_array = []

    # Get list of files in the bucket, return list. Break if chunk size or end of file list.
    for object_summary in s3_bucket.objects.filter(Prefix=s3_folder):
        file_name_array.append(object_summary.key)
        file_counter += 1
        if (file_counter % 1000) == 0:
            print(file_counter)
        if file_counter == chunk_size:
            break
    return file_name_array


# Simple method to write a list of file names to a text file
def write_file_names_to_text_file(file_name_array, path, file_name):
    with open(path + file_name, 'w') as txt_file:
        for i in range(len(file_name_array)):
            txt_file.write(file_name_array[i])
            txt_file.write('\n')


# Method to open the gz file, read the file, and get the number of lines by counting the newline char
# Remember, if reading a wtj csv file, the first row/line is the header with column names
def get_s3_gz_file_line_count(aws_session_resource, s3_bucket, object_key):
    file_object = aws_session_resource.Object(s3_bucket, object_key)
    total_lines = 0
    with gzip.GzipFile(fileobj=file_object.get()["Body"]) as gzip_file:
        content = gzip_file.read()
        lines = content.decode('utf8').count('\n')
        total_lines += lines
    return total_lines


# Method to open the gz file, read the file, and output each line
def insert_s3_gz_file_contents(conn, fileid, aws_session_resource, s3_bucket_name, object_key, field_data_types):

    try:
        # Open gz from s3
        file_object = aws_session_resource.Object(s3_bucket_name, object_key)
        gzipped = gzip.GzipFile(None, 'rb', fileobj=file_object.get()["Body"])
        data = TextIOWrapper(gzipped)
    except:
        print('Cannot get bucket info for ')
        print(s3_bucket_name)
        return -1

    row_number = 0
    field_names = []

    # For each line in the file, split by the tilde character
    # so now each line in the file is an array of values
    # First line in the file are the column headers
    for row in data:
        items = row.replace('\n','').split('~')
        # Get the header row field names
        if row_number == 0:
            field_names = items
            # print(field_names)
        else:
            # Process each element of the row
            return_code = insert_wtj_row(conn, fileid, field_names, items, field_data_types)
            if return_code != 0:
                # something bad happened
                print('something bad happened processing row')
                return -1
        row_number += 1

    # Return with a success
    return 0


# Method to get the total number of file in an S3 bucket
def get_s3_total_file_count(s3_bucket):
    # use loop and count increment
    count_obj = 0
    for i in s3_bucket.objects.all():
        count_obj = count_obj + 1
    return count_obj


