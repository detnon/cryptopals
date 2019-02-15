import codecs

h1 = '1c0111001f010100061a024b53535009181c'
h2 = '686974207468652062756c6c277320657965'
dh1 = (codecs.decode(h1, 'hex'))
dh2 = (codecs.decode(h2, 'hex'))


print(h1)
print(dh1)
for i in dh1:
    print(format(ord(i), '08b'))


print(h2)
print(dh2)
for i in dh2:
    print(format(ord(i), '08b'))


x = ord(dh1[0]) ^ ord(dh2[0])

print(x)
print(format(x, '08b'))

print(codecs.encode(chr(x), 'hex'))
bh1 = ""
bh2 = ""
xord = ""

for i in xrange(0, len(dh1)):
    xord += chr(ord(dh1[i]) ^ ord(dh2[i]))

print(xord)
print(codecs.encode(xord, 'hex'))
