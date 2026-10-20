s=input("Message: ")
k=int(input("Shift: "))%26
e=""
d=""
for c in s:
 if c.isupper():
  e+=chr((ord(c)-65+k)%26+65)
 elif c.islower():
  e+=chr((ord(c)-97+k)%26+97)
 else:
  e+=c
for c in e:
 if c.isupper():
  d+=chr((ord(c)-65-k)%26+65)
 elif c.islower():
  d+=chr((ord(c)-97-k)%26+97)
 else:
  d+=c
print("Encrypted:",e)
print("Decrypted:",d)