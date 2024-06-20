'''
ip:
    s="khoor"
    
    key=3
'''
'''
print(97%26)
s=input()
decrypt=""
key=52
for i in s:
    decrypt=decrypt+chr((ord(i)-key-97)%26+97)
print(decrypt)
    '''
s=input()
key=3
c=key%26
decrypt=""
for i in s:
    if (ord(i)-(key%26))>=97:
        decrypt=decrypt+chr(ord(i)-c)
    else:
        decrypt=decrypt+chr(ord(i)-c+26)
print(decrypt)
