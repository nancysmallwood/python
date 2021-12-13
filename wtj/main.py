# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from apps.oseriescsv import read_dataset_csv, read_dataelement_csv
from apps.postgresql import test_connect, get_data_source_version, get_data_source_domain, get_storage_instance

path = 'C:\\githubrepos\\arch-et-datainventory-catalog\\dataPlatfom\\metaData\\sampleDataSets\\'
testdatasetfile = 'C:\\githubrepos\\arch-et-datainventory-catalog\\dataPlatfom\\metaData\\sampleDataSets\\RPTdataset.csv'
testelementfile = 'C:\\githubrepos\\arch-et-datainventory-catalog\\dataPlatfom\\metaData\\sampleDataSets\\RPTcolumns.csv'


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # read_dataset_csv(testdatasetfile)
    # read_dataelement_csv(testelementfile)
    #read_dataset_csv(path + 'UTILdataset.csv')
    # read_dataelement_csv(path + 'UTILcolumns.csv')
    # read_dataset_csv(path + 'TPSdataset.csv')
    # read_dataelement_csv(path + 'TPScolumns.csv')
    # read_dataset_csv(path + 'RTEdataset.csv')
    read_dataelement_csv(path + 'GIScolumns.csv')
    read_dataelement_csv(path + 'RPTcolumns.csv')
    read_dataelement_csv(path + 'TaxJournalcolumns.csv')
    read_dataelement_csv(path + 'UTILcolumns.csv')
    read_dataelement_csv(path + 'TPScolumns.csv')
    read_dataelement_csv(path + 'RTEcolumns.csv')
    # test_connect()
    # data_source = get_data_source_version('O Series Database Data Models 9.0 SR4')
    # data_source_domain = get_data_source_domain('Utility',data_source[0], data_source[1])
    # storage_instance = get_storage_instance('oseriesUtilTables.csv', data_source[0], data_source[1])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
