import gzip
import os
import sys


def unzip_file(filename):
    # Open gz
    try:
        with gzip.open(filename, 'rb') as f_in:
            prefix, extension = os.path.splitext(filename)
            new_file = open(prefix + ".csv","w", encoding='utf-8')
            new_file.write(f_in.read().decode("utf-8", errors='ignore'))
            new_file.close()
            print (f"File extracted as \"{new_file.name}\"")
    except OSError as e:
        print(f"File open error. Does file \"{filename}\" exist?")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Missing filename")
    else:
        unzip_file(sys.argv[1])
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
    # unzip_file('PyCharm')
