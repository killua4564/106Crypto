import base64
import random
import hashlib

flag = 'flag{xxxxxxxxxxxxxxxxxxxxxxxx}'

def no_flag(string):
	return string[4:].strip('{}')

def func(string):
	return ''.join('{:02x}'.format(ord(i)) for i in string)

def base_32(string):
	return str(base64.b32encode(bytes(flag, 'utf-8')))[2:-1]

def base_64(string):
	return str(base64.b64encode(bytes(flag, 'utf-8')))[2:-1]

def md5(string):
	return hashlib.md5(bytes(string, 'utf-8')).hexdigest()

def sha1(string):
	return hashlib.sha1(bytes(string, 'utf-8')).hexdigest()

def sha256(string):
	return hashlib.sha256(bytes(string, 'utf-8')).hexdigest()

def sha512(string):
	return hashlib.sha512(bytes(string, 'utf-8')).hexdigest()

def magic(string):
	return string[::-1]

E = [func, base_32, base_64, md5, sha1, sha256, sha512, magic]

if __name__ == '__main__':
	
	flag = no_flag(flag)

	for i in range(1, random.randint(3, 6)):
		flag = E[random.randint(0, len(E)-1)](flag)

	open('flag2', 'w').write(flag)


