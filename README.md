# encrypt-and-decrypt
This Python script implements a simple Caesar cipher, which is a type of substitution cipher where each letter in the plaintext is shifted by a certain number of positions down or up the alphabet. Here's a breakdown of how the code works:

Components:
1. alpha_list:
A list containing the alphabet twice, making it easier to handle shifts without worrying about wrapping around the end of the list.
2. encrypt(cipher_text, key):
Takes in cipher_text (the text to be encrypted) and a key (the number of positions to shift).
For each letter in cipher_text, it finds the index in alpha_list and adds the key to get the shifted letter.
Spaces in the text are preserved.
The encrypted text is printed.
3. decrypt(cipher_text, key):
Works similarly to encrypt, but shifts the letters in the opposite direction by subtracting the key.
The decrypted text is printed.
4. User Inputs:
cipher_text: The text to be encrypted or decrypted.
key: The shift amount.
operation: The user specifies whether they want to "encrypt" or "decrypt" the text.
5. Key Handling:
The key is taken modulo 26 (key = key % 26) to ensure it wraps around properly, as there are 26 letters in the alphabet.
Execution:
Depending on the operation chosen by the user (encrypt or decrypt), the corresponding function is called with the provided cipher_text and key.

Example:
If you input "hello" as the cipher_text, with a key of 3, and choose encrypt, the output would be "khoor".
If you decrypt "khoor" with the same key, the output would be "hello".
This script provides a straightforward implementation of the Caesar cipher, allowing for both encryption and decryption of text with a specified key.
