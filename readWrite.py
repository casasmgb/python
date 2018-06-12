#! /usr/bin/env python3

from smartcard.System import readers
# define the APDUs used in this script
COMMAND = [0xFF, 0xCA, 0x00, 0x00, 0x00]
LOAD_KEY = [0xFF, 0x82, 0x20, 0x01, 0x06, 0xFF , 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
AUTHENTICATE =[0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x01, 0x60, 0x01]

def write(reader):
    print ('write')
    try:
        DATA = [0x53, 0x61, 0x79, 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x4d, 0x79, 0x46, 0x72, 0x69, 0x65, 0x6e, 0x64 ]
        WRITE = [0xFF, 0xF4, 0x00, 0x01]
        connection = reader.createConnection()
        connection.connect()
        data, sw1, sw2 = connection.transmit(WRITE)
        print('data', data, 'sw1', sw1, 'sw2', sw2)
    except Exception:
        print ("No card detected. ")

def read(reader):
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
    print ("AUTHENTICATION")
    try:
        LOAD_KEY = [0xFF, 0x82, 0x20, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x00, 0x61, 0x00]
        READ = [0xFF, 0xB0, 0x00, 0x02, 0x10]
        connection = reader.createConnection()
        connection.connect()
        data, sw1, sw2 = connection.transmit(LOAD_KEY)
        print('data', data, 'sw1', sw1, 'sw2', sw2)
        data, sw1, sw2 = connection.transmit(AUTH)
        print('data', data, 'sw1', sw1, 'sw2', sw2)
        data, sw1, sw2 = connection.transmit(READ)
        print('data', data, 'sw1', sw1, 'sw2', sw2)
    except Exception:
        print ("No card detected. ")

def loadK():
    print ("LOAD KEY")

# get all the available readers
r = readers()
print ("Available readers:", r)

reader = r[0]
print ("Using:", reader)
auth(reader)
#read(reader)
#write(reader)
