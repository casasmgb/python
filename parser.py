#! /usr/bin/env python3
import sys
print(bytearray.fromhex("4345445541204445204944454e54494444a45535441444f20504c5552494e41494f4e414c20444520424f4c495649414fa4d45524c4fa343330353535342d30a424f4c495649414e41a30342d312d31393831a4d415343554c494e4fa442f59473950594f71394e5543757756553573785a4a643371466e43434c586462342b4453757342694535777043374f545979654837784977507950512f592b4930544376343668612b2b2f4236754a496b42534f33597855634e30624977476a2f556f3263502f646258775a725a526a3942555a5a5a4f4c33383d").decode())
# print(bytes.fromhex('4345445541204445204944454e54494441447c45535441444f20504c5552494e4143494f4e414c20444520424f4c495649410a415249454c204d4152434f530a434f4e444f0a4d45524c4f0a3433').decode('utf-8'))
# s = 'CEDULA DE IDENTIDAD\nESTADO PLURINACIONAL DE BOLIVIA\nARIEL MARCOS\nCONDO\nMERLO\n4305554-I0\nBOLIVIANA\n04-12-1981\nMASCULINO\n04-12-2025\nfddAgBhD/YG9PYOq9NUCuwVKU5sxZJd3qFnCCLXd3b4+DSusBiE5wpC7OIcBQ21awNTdZQpWdgOTYyeH7xIwPyPQ/Y+BI0TCv46ha++/B6uJNIkBSO3YxUcN0bIwGuvSwNpcJzYKtksddhEj/Uo2cP/dbXwZrZRlj9BUZZZOL38='.encode('utf-8')
# hexTexto = []
# for letra in s:
#     hexTexto.append(letra)
# print (hexTexto)
# # print (s.hex())
# # print(bytes.fromhex(s.hex()).decode('utf-8'))
# for i in hexTexto:
#     print(hex(i))

# hexTexto = []
# if len(sys.argv)>1:
#     directorio=sys.argv[1]
#     filename = directorio

#     with open(filename) as f: content = f.readlines()
#     texto = ''
#     for line in content: texto += line
#     texto = texto.encode('utf-8')
#     for letra in texto:
#         hexTexto.append(hex(letra))
#     print(hexTexto)