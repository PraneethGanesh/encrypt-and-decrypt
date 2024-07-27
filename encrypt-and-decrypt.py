# encrypt-and-decrypt
alpha_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(cipher_text,key):
 encrypt_text=" "
 for letter in cipher_text:
  if letter==" ":
   encrypt_text+=" "
  else:
   i=alpha_list.index(letter)
   encrypt_text+=alpha_list[i+key]
 print(encrypt_text)   
def decrypt(cipher_text,key):
 decrypt_text=" "
 for letter in cipher_text:
  if letter==" ":
   decrypt_text+=" "
  else:
   i=alpha_list.index(letter)
   decrypt_text+=alpha_list[i-key]
 print(decrypt_text)    
x=alpha_list.index('a')
cipher_text=input("enter cipher text:").lower()
key=int(input("enter key:"))
key=key%26
operation=input("encrypt\decrypt: ").lower()
if operation=="encrypt":
 encrypt(cipher_text,key)
elif operation=="decrypt":
 decrypt(cipher_text,key) 
