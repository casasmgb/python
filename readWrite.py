#! /usr/bin/env python3

from smartcard.System import readers

def readUUID(reader):
    COMMAND = [0xFF, 0xCA, 0x00, 0x00, 0x00]
    print ("READ")
    try:
        connection = reader.createConnection()
        connection.connect()
        data, sw1, sw2 = connection.transmit(COMMAND)
        print ("UID[]:", data)
        print ("UID h:", " ".join(['{:02X}'.format(h) for h in data]))
        print ("Command: %02X %02X" % (sw1, sw2))
        print('data', data, 'sw1', sw1, 'sw2', sw2)
    except Exception:
        print ("No card detected. ")

def authAndWrite(reader):
    print ("AUTHENTICATION AND WRITE")
    try:
        # LOAD_KEY = [0xFF, 0x82, 0x20, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        # AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x08, 0x60, 0x00]
        #                                                   ^blo
        # WRITE = [0xFF, 0xD6, 0x00, 0x08, 0x10, 0x53, 0x61, 0x79, 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x4d, 0x79, 0x46, 0x72, 0x69, 0x65, 0x6e, 0x64]
        #                            ^sec        ______________________________________________________________________________________________DATA
        LOAD_KEY = [0xFF, 0x82, 0x20, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x08, 0x60, 0x00]
        WRITE = [0xFF, 0xD6, 0x00, 0x08, 0x10, 0x53, 0x61, 0x79, 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x4d, 0x79, 0x46, 0x72, 0x69, 0x65, 0x6e, 0x64]
        connection = reader.createConnection()
        connection.connect()
        data, sw1, sw2 = connection.transmit(LOAD_KEY)
        print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
        data, sw1, sw2 = connection.transmit(AUTH)
        print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
        data, sw1, sw2 = connection.transmit(WRITE)
        print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
    except Exception:
        print ("No card detected. ")

def authAndRead(reader):
    print ("AUTHENTICATION AND READ")
    try:
        # LOAD_KEY = [0xFF, 0x82, 0x20, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        # AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x08, 0x60, 0x00]
        # READ = [0xFF, 0xB0, 0x00, 0x08, 0x10]

        LOAD_KEY = [0xFF, 0x82, 0x20, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x08, 0x60, 0x00]
        READ = [0xFF, 0xB0, 0x00, 0x08, 0x10]
        connection = reader.createConnection()
        connection.connect()
        data, sw1, sw2 = connection.transmit(LOAD_KEY)
        print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
        data, sw1, sw2 = connection.transmit(AUTH)
        print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
        data, sw1, sw2 = connection.transmit(READ)
        print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
    except Exception:
        print ("No card detected. ")

# get all the available readers
r = readers()
print ("Available readers:", r)

reader = r[0]
print ("Using:", reader)
# authAndWrite(reader)
authAndRead(reader)
#read(reader)
#write(reader)
