#Nama       : Rehan Aziz Hardiansyah
#NPM        : 140810240075
#Deskripsi  : program untuk enkripsi, dekripsi, dan mencari kunci Hill Cipher

import numpy as np

def modInverse(a, m=26):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Tidak ada invers modulo untuk {a} mod {m}")

def matrixModInv(matrix, modulus=26):
    det = int(np.round(np.linalg.det(matrix))) % modulus
    detInv = modInverse(det, modulus)
    
    # matrix ordo 2x2
    adj = np.array([
        [matrix[1, 1], -matrix[0, 1]],
        [-matrix[1, 0], matrix[0, 0]]
    ]) % modulus
    
    return (detInv * adj) % modulus

def textToMatrix(text, blockSize=2):
    nums = [ord(c.upper()) - ord('A') for c in text if c.isalpha()]
    while len(nums) % blockSize != 0:
        nums.append(ord('X') - ord('A')) # Padding huruf X
    
    blocks = [nums[i:i + blockSize] for i in range(0, len(nums), blockSize)]
    return np.array(blocks).T

def matrixToText(matrix):
    flatMatrix = matrix.T.flatten()
    return "".join([chr(int(n) % 26 + ord('A')) for n in flatMatrix])

def encryptHill(plainText, keyMatrix):
    P = textToMatrix(plainText, keyMatrix.shape[0])
    C = (np.dot(keyMatrix, P)) % 26
    return matrixToText(C)

def decryptHill(cipherText, keyMatrix):
    KInv = matrixModInv(keyMatrix, 26)
    C = textToMatrix(cipherText, keyMatrix.shape[0])
    P = (np.dot(KInv, C)) % 26
    return matrixToText(P)

def findKeyHill(plainText, cipherText, blockSize=2):
    P = textToMatrix(plainText, blockSize)[:, :blockSize]
    C = textToMatrix(cipherText, blockSize)[:, :blockSize]
    
    PInv = matrixModInv(P, 26)
    K = (np.dot(C, PInv)) % 26
    return K.astype(int)

if __name__ == "__main__":
    while True:
        print("=== PROGRAM HILL CIPHER (2x2) ===")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Cari Kunci (Known Plaintext Attack)")
        print("0. Keluar")
        pilihanMenu = input("Pilih menu: ")

        if pilihanMenu == "1":
            plainText = input("Masukkan Plaintext: ")
            k11, k12 = map(int, input("Baris 1 kunci (misal 7 6): ").split())
            k21, k22 = map(int, input("Baris 2 kunci (misal 2 5): ").split())
            keyMatrix = np.array([[k11, k12], [k21, k22]])
            print("Ciphertext:", encryptHill(plainText, keyMatrix))
            
        elif pilihanMenu == "2":
            cipherText = input("Masukkan Ciphertext: ")
            k11, k12 = map(int, input("Baris 1 kunci (misal 1 3): ").split())
            k21, k22 = map(int, input("Baris 2 kunci (misal 0 4): ").split())
            keyMatrix = np.array([[k11, k12], [k21, k22]])
            print("Plaintext:", decryptHill(cipherText, keyMatrix))
            
        elif pilihanMenu == "3":
            plainText = input("Masukkan Plaintext sampel (min. 4 huruf): ")
            cipherText = input("Masukkan Ciphertext sampel (min. 4 huruf): ")
            keyMatrix = findKeyHill(plainText, cipherText)
            print("Matriks Kunci Ditemukan:\n", keyMatrix)   
            
        elif pilihanMenu == "0":
            print("Terima kasih! Program selesai.")
            break
            
        else:
            print("PERINGATAN: Pilihan menu tidak valid! Program otomatis dihentikan.")
            break