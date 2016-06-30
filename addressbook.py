from __future__ import print_function
import os
import capnp
from datetime import datetime

import addressbook_capnp

def writeAddressBook(file):
    addresses = addressbook_capnp.AddressBook.new_message()
    people = addresses.init('people', 2)

    alice = people[0]
    alice.id = 123
    alice.name = 'Alice'
    alice.email = 'alice@example.com'
    alicePhones = alice.init('phones', 1)
    alicePhones[0].number = "555-1212"
    alicePhones[0].type = 'mobile'
    alice.employment.school = "MIT"

    bob = people[1]
    bob.id = 456
    bob.name = 'Bob'
    bob.email = 'bob@example.com'
    bobPhones = bob.init('phones', 2)
    bobPhones[0].number = "555-4567"
    bobPhones[0].type = 'home'
    bobPhones[1].number = "555-7654"
    bobPhones[1].type = 'work'
    bob.employment.unemployed = None

    s1 = datetime.now()
    addresses.write(file)
    s2 = datetime.now()
    print("Time to write: {}".format(s2 - s1))

def printAddressBook(file):
    s1 = datetime.now()
    addresses = addressbook_capnp.AddressBook.read(file)
    s2 = datetime.now()
    print("Time to read: {}".format(s2 - s1))

    for person in addresses.people:
        print(person.name, ':', person.email)
        for phone in person.phones:
            print(phone.type, ':', phone.number)

        which = person.employment.which()
        print(which)

        if which == 'unemployed':
            print('unemployed')
        elif which == 'employer':
            print('employer:', person.employment.employer)
        elif which == 'school':
            print('student at:', person.employment.school)
        elif which == 'selfEmployed':
            print('self employed')
        print()


if __name__ == '__main__':
    f = open('example', 'w')
    writeAddressBook(f)

    f = open('example', 'r')
    printAddressBook(f)
