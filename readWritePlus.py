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

def auth(reader):
    print ("AUTHENTICATION AND WRITE")
    try:
        AUTH = [0x70, 0x04, 0x40, 0x06, 0x29, 0x06, 0x34, 0x10, 0x01, 0x04]
        connection = reader.createConnection()
        connection.connect()
        data, sw1, sw2 = connection.transmit(AUTH)
        print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
    except Exception as e:
        print ("No card detected. OR ############", e)
    print ("===========================================================")

# get all the available readers
r = readers()
print ("Available readers:", r)

reader = r[0]
print ("Using:", reader)
#authAndWrite(reader)
auth(reader)
#read(reader)
#authAndReadMifare(reader)