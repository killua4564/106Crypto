import binascii
import string
import base64

def rot13(s):
    return s.translate(s.maketrans(string.ascii_uppercase + string.ascii_lowercase, 
    	string.ascii_uppercase[13:] + string.ascii_uppercase[:13] + 
    	string.ascii_lowercase[13:] + string.ascii_lowercase[:13]))

def base(s):
	return str(base64.b64decode(s))[2:-1]

def hex(s):
    return str(binascii.unhexlify(s))[2:-1]

def upsidedown(s):
    return s.translate(s.maketrans(string.ascii_uppercase + string.ascii_lowercase, 
    	string.ascii_lowercase + string.ascii_uppercase))

if __name__ == '__main__':
	E = (rot13, base, hex, upsidedown)
	flag = open('flag.enc', 'r').read()
	while not flag.startswith('FLAG{') and not flag.startswith('flag{'):
		n, flag = int(flag[0]), flag[1:]
		flag = E[n](flag)

print(flag)