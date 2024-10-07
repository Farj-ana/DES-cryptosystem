from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def encrypt_my_file(key, input_file, output_file):
    with open(input_file, 'rb') as f:
        ptxt = f.read()
    
    #<============================================================ Creating DES cipher object
    cipher = DES.new(key, DES.MODE_ECB)
    
    #<============================================================= this is for Encrypt plaintext
    ctxt = cipher.encrypt(pad(ptxt, DES.block_size))
    
    #<=========================================================== for Converting ciphertext to hexadecimal for readability
    hex_ctxt = binascii.hexlify(ctxt).decode('utf-8')
    
    with open(output_file, 'w') as f:
        f.write(hex_ctxt)

    print("Encryption is complete.\nSaved file name is:", output_file)
    print("Student Name: Farjana")
    print("Student Number: 100******")

def decrypt_my_file(key, input_file, output_file):
    with open(input_file, 'r') as f:
        hex_ctxt = f.read()
    
    #<============================================================= for Converting the hex ciphertext to bytes
    try:
        ctxt = binascii.unhexlify(hex_ctxt)
    except binascii.Error as e:
        print("Error!\nDuring hex to bytes:", e)
        return

    #<============================================================= DES cipher object for DES encryption and decryption
    cipher = DES.new(key, DES.MODE_ECB)
    
    try:
        #<=========================================================== Decrypt and remove padding
        ptxt = unpad(cipher.decrypt(ctxt), DES.block_size)
    except ValueError as e:
        print("Error!\nDuring unpadding:", e)
        return
    
    with open(output_file, 'wb') as f:
        f.write(ptxt)

    print("Decryption is complete.\nSaved file name is:", output_file)
    print("Student Name: Farjana")
    print("Student Number: 100******")


def main():
    
    secret_key = input("Enter 8-byte (64-bit) key: ").encode()  
    
    if len(secret_key) != 8:
        print("Invalid key length.")
        return
    
    operation = input("What do you want? Encrypt or Decrypt (E/D)? ").upper()
    
    if operation == 'E':
        input_file = input("Enter the file name for encrypt: ")
        output_file = input("Enter the output file name where it will save: ")
        encrypt_my_file(secret_key, input_file, output_file)
        
    elif operation == 'D':
        input_file = input("Enter the file name for decrypt: ")
        output_file = input("Enter the output file name where it will save : ")
        decrypt_my_file(secret_key, input_file, output_file)
        
    else:
        print("Invalid. Please enter 'E' for encryption or 'D' for decryption.")
    
if __name__ == "__main__":
    main()

