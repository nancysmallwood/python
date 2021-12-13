# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import uuid


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    urn_guy = uuid.uuid4()
    print('URN')
    print(urn_guy.urn)
    print(urn_guy.variant)
    print(urn_guy.version)
    urn_gal = uuid.uuid5(uuid.NAMESPACE_DNS, 'vertexinc')
    print(urn_gal.urn)
    print(urn_gal.variant)
    print(urn_gal.version)
    print(urn_gal.fields)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
