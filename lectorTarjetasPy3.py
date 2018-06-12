#! /usr/bin/env python3

from smartcard.System import readers
# define the APDUs used in this script
COMMAND = [0xFF, 0xCA, 0x00, 0x00, 0x00]

# get all the available readers
r = readers()
print ("Available readers:", r)

reader = r[0]
print ("Using:", reader)

try:
    connection = reader.createConnection()
    connection.connect()
    data, sw1, sw2 = connection.transmit(COMMAND)
    print ("UID[]:", data)
    print ("UID h:", " ".join(['{:02X}'.format(h) for h in data]))
    print ("Command: %02X %02X" % (sw1, sw2))
    print ("90 00 is ok")
except ValueError:
    print ("No card detected. ", ValueError)
