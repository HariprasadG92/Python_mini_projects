from logo import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(text, shift, direction):
    cipher_txt = ""
    # print(list(text)) # just for reference
    for k in text:
        if k in alphabet:
            pos = alphabet.index(k)
            if direction == "encode":
                new_pos = pos + shift
            else:
                new_pos = pos - shift
            new_let = alphabet[new_pos]
            cipher_txt += new_let
        else:
            cipher_txt += k
    print(f"The {direction}d message: {cipher_txt}")

end_cipher = True
while end_cipher:
    cip = input("Type 'Encode' to encrypt, type ' Decode' to decrypt:\n").lower()
    txt = input("Type your message:\n").lower()
    sft = int(input("Enter the number of shifts:\n"))
    sft = sft % 26
    cipher(text = txt, shift=sft, direction = cip)
    
    end = input("Do you want to continue? (yes/no)\n").lower()
    
    if end == "no":
        end_cipher = False
        print("Cipher coding completed successfully")

# 5: etwt
