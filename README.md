
# DES Encryption and Decryption Program

## Overview
This project implements a **DES (Data Encryption Standard)** encryption and decryption tool in Python. It enables you to securely encrypt or decrypt data stored in a file using a custom cryptographic key. The program reads from plaintext (`plain.txt`) or ciphertext (`cipher.txt`) files and assumes the file size is a multiple of 64 bits, as required by the DES algorithm.

## Features
- **DES Encryption and Decryption:** Utilizes the DES algorithm for symmetric key cryptography.
- **File-based Input/Output:** Encrypts and decrypts files such as `plain.txt` (for plaintext) and `cipher.txt` (for ciphertext).
- **User-defined Key:** The program accepts a user-provided 64-bit cryptographic key for the encryption or decryption process.
- **Pythonic Implementation:** Built using Python and the `cryptography` library to perform secure DES operations.

## Requirements
- **Python 3.12.6**
- **cryptography** library (install via `pip install cryptography`)

## Usage

### Clone the Repository:
```bash
git clone https://github.com/yourusername/DES-encryption-decryption.git
```

### Install Dependencies:
```bash
pip install cryptography
```

### Prepare Input File:
- Place the plaintext to be encrypted in a file named `plain.txt`, or the ciphertext for decryption in `cipher.txt`.

### Run the Program:

#### Encrypting:
```bash
python des_encrypt.py key plain.txt
```

#### Decrypting:
```bash
python des_decrypt.py key cipher.txt
```

### View Output:
- The program will output the results in either a new ciphertext or plaintext file.

## Example

To encrypt a file called `plain.txt` with a key `12345678`:

```bash
python des_encrypt.py 12345678 plain.txt
```

To decrypt the generated ciphertext file with the same key:

```bash
python des_decrypt.py 12345678 cipher.txt
```

## Screenshot
A screenshot with my full name and student number is attached in the repository to demonstrate successful execution.
![alt text](https://raw.githubusercontent.com/Farj-ana/DES-cryptosystem/refs/heads/main/Screenshot.png)

## References
- [DES Encryption Documentation](https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/?highlight=des)
- [Understanding DES](https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/)
- [Reading and Writing Files in Python](https://realpython.com/read-write-files-python/)

## License
This project is open-source and licensed under the MIT License.
