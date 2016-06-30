import addressbook_pb2
from datetime import datetime

def writeAddressBook(f):

    addresses = addressbook_pb2.AddressBook()

    alice = addresses.people.add()
    alice.id = 123
    alice.name = 'Alice'
    alice.email = "alice@example.com"
    phone = alice.phones.add()
    phone.number = "555-1212"
    # phone.type = phone.MOBILE
    alice.school = "MIT"

    bob = addresses.people.add()
    bob.id = 456
    bob.name = 'Bob'
    bob.email = 'bob@example.com'
    bobPhone0 = bob.phones.add()
    bobPhone0.number = "555-4567"
    # bobPhone0.type = phone.HOME
    bobPhone1 = bob.phones.add()
    bobPhone1.number = "555-7654"
    # bobPhone1.type = phone.WORK
    bob.unemployed = True

    s1 = datetime.now()
    f.write(addresses.SerializeToString())
    s2 = datetime.now()
    print("Time to write: {}".format(s2 - s1))

def printAddressBook(f):

    addresses = addressbook_pb2.AddressBook()
    
    s1 = datetime.now()
    addresses.ParseFromString(f.read())
    s2 = datetime.now()
    print("Time to read: {}".format(s2 - s1))

    for person in addresses.people:
        print(person.name, ':', person.email)
        for phone in person.phones:
            print(phone.type, ':', phone.number)


if __name__ == '__main__':
    fname = "example.proto"
    f = open(fname, 'w')
    writeAddressBook(f)

    f = open(fname, 'r')
    printAddressBook(f)