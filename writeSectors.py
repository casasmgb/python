#! /usr/bin/env python3
import sys
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

def authAndWriteMifare(reader, texto):
    print ("AUTHENTICATION AND WRITE")
    try:
        # LOAD_KEY = [0xFF, 0x82, 0x20, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        # AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x08, 0x60, 0x00]
        #                                                   ^blo
        # WRITE = [0xFF, 0xD6, 0x00, 0x08, 0x10, 0x53, 0x61, 0x79, 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x4d, 0x79, 0x46, 0x72, 0x69, 0x65, 0x6e, 0x64]
        #                            ^blo        ______________________________________________________________________________________________DATA
        connection = reader.createConnection()
        connection.connect()

        LOAD_KEY = [0xFF, 0x82, 0x20, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        data, sw1, sw2 = connection.transmit(LOAD_KEY)
        print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
        marca = 16
        cont = 0
        for i in range(16, 127):
            if cont >= len(texto):
                print (i-16, 'ALTO...!!!')
                break
            if (i != marca+3):
                AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, i, 0x60, 0x00]
                WRITE = [0xFF, 0xD6, 0x00, i, 0x10, texto[cont][0], texto[cont][1], texto[cont][2], texto[cont][3], texto[cont][4], texto[cont][5], texto[cont][6], texto[cont][7], texto[cont][8], texto[cont][9], texto[cont][10], texto[cont][11], texto[cont][12], texto[cont][13], texto[cont][14], texto[cont][15]]
                data, sw1, sw2 = connection.transmit(AUTH)
                #print('AUTH:::::Bloque:::::', i,  'data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
                data, sw1, sw2 = connection.transmit(WRITE)
                print('WRITE::::Bloque:::::',i,  'data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
                cont = cont +1
            else:
                marca = marca+4
        # AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x30, 0x60, 0x00]
        # WRITE = [0xFF, 0xD6, 0x00, 0x30, 0x10, 0xFE, 0xEA, 0x01, 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x4d, 0x79, 0x46, 0x72, 0x69, 0x65, 0x6e, 0x64]        
        # data, sw1, sw2 = connection.transmit(AUTH)
        # print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
        # data, sw1, sw2 = connection.transmit(WRITE)
        # print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))

    except Exception:
        print ("No card detected. ")
    print ("===========================================================")

def authAndEraceMifare4K(reader):
    print ("AUTHENTICATION AND ERACE")
    try:
        # LOAD_KEY = [0xFF, 0x82, 0x20, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        # AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x08, 0x60, 0x00]
        #                                                   ^blo
        # WRITE = [0xFF, 0xD6, 0x00, 0x08, 0x10, 0x53, 0x61, 0x79, 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x4d, 0x79, 0x46, 0x72, 0x69, 0x65, 0x6e, 0x64]
        #                            ^blo        ______________________________________________________________________________________________DATA
        connection = reader.createConnection()
        connection.connect()

        LOAD_KEY = [0xFF, 0x82, 0x20, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        data, sw1, sw2 = connection.transmit(LOAD_KEY)
        print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
        marca = 16
        marca = 16
        for i in range(16, 127):
            if (i != marca+3):
                AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, i, 0x60, 0x00]
                WRITE = [0xFF, 0xD6, 0x00, i, 0x10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                data, sw1, sw2 = connection.transmit(AUTH)
                print('AUTH:::::Bloque:::::', i,  'data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
                data, sw1, sw2 = connection.transmit(WRITE)
                print('WRITE::::Bloque:::::',i,  'data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
            else:
                marca = marca+4

    except Exception:
        print ("No card detected. ")
    print ("===========================================================")

def authAndEraceMifare1K(reader):
    print ("AUTHENTICATION AND ERACE")
    try:
        # LOAD_KEY = [0xFF, 0x82, 0x20, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        # AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x08, 0x60, 0x00]
        #                                                   ^blo
        # WRITE = [0xFF, 0xD6, 0x00, 0x08, 0x10, 0x53, 0x61, 0x79, 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x4d, 0x79, 0x46, 0x72, 0x69, 0x65, 0x6e, 0x64]
        #                            ^blo        ______________________________________________________________________________________________DATA
        connection = reader.createConnection()
        connection.connect()

        LOAD_KEY = [0xFF, 0x82, 0x20, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        data, sw1, sw2 = connection.transmit(LOAD_KEY)
        print('data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
        marca = 16
        for i in range(16, 63):
            if (i != marca+3):
                AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, i, 0x60, 0x00]
                WRITE = [0xFF, 0xD6, 0x00, i, 0x10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                data, sw1, sw2 = connection.transmit(AUTH)
                print('AUTH:::::Bloque:::::', i,  'data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
                data, sw1, sw2 = connection.transmit(WRITE)
                print('WRITE::::Bloque:::::',i,  'data', data, 'sw1', hex(sw1), 'sw2', hex(sw2))
            else:
                marca = marca+4

    except Exception:
        print ("No card detected. ")
    print ("===========================================================")

def getHex(dir):
    hexTexto = []
    with open(dir) as f: content = f.readlines()
    texto = ''
    for line in content: texto += line
    texto = texto.encode('utf-8')
    block=[]
    count = 0
    for letra in texto:
        if (count <15):
            block.append(letra)
            count = count+1
        else:
            block.append(letra)
            hexTexto.append(block)
            count = 0
            block=[]
    for j in range (len(block), 16):
        block.append(0)
    hexTexto.append(block)
    return hexTexto

# get all the available readers
r = readers()
print ("Available readers:", r)
reader = r[0]
print ("Using:", reader)
if len(sys.argv)>1:
    directorio=sys.argv[1]
    textToHex = getHex(directorio)
    print(textToHex)
    authAndWriteMifare(reader, textToHex)
    #authAndEraceMifare1K(reader)
    #authAndEraceMifare4K(reader)