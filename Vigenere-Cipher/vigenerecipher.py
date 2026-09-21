#Nama       : Rehan Aziz Hardiansyah
#NPM        : 140810240075
#Deskripsi  : program untuk enkripsi dan dekripsi Vigenere Cipher

def vigenere_enkripsi(plainText, key):
    cipherText = []
    key = key.upper()
    key_index = 0
    
    for char in plainText:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            
            shift = ord(key[key_index % len(key)]) - ord('A')
            
            enkripsi = chr((ord(char) - start + shift) % 26 + start)
            cipherText.append(enkripsi)
            
            key_index +=1
        else:
            cipherText.append(char)
    return "".join(cipherText)    

def vigenere_dekripsi(plainText, key):
    cipherText = []
    key = key.upper()
    key_index = 0
    
    for char in plainText:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            
            shift = ord(key[key_index % len(key)]) - ord('A')
            
            enkripsi = chr((ord(char) - start - shift) % 26 + start)
            cipherText.append(enkripsi)
            
            key_index +=1
        else:
            cipherText.append(char)
    return "".join(cipherText)

def main():
    pt = "ASPRAKGANTENG"
    k = "REHANAZIZHARD"
    
    enkripsi = vigenere_enkripsi(pt, k)
    print(f"Teks Asli  : {pt}")
    print(f"Kunci      : {k}")
    print(f"Enkripsi   : {enkripsi}")
    
    dekripsi = vigenere_dekripsi(enkripsi, k)
    print(f"Dekripsi   : {dekripsi}")
    
main()