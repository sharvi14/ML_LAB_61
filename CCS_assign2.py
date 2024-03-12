import math

p = int(input('Enter the value of the P '))
q = int(input('Enter the value of the q '))

if p % 2 != 0 and q % 2 != 0:
    m = int(input('Enter the value of m '))
    e = int(input('Enter the value of e '))
    n = p * q
    phi = (p - 1) * (q - 1)
    c = (m ** e) % n
    print("Encrypted message:", c)
    
    # Calculate the private key 'd' using modular inverse
    d = pow(e, -1, phi)
    
    mn = (c ** d) % n
    print("Decrypted message:", mn)
else: 
    print('invalid')