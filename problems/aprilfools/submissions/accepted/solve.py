A_INT = ord("A")
Z_INT = ord("Z")
ALPHABET_LENGTH = Z_INT - A_INT + 1
N = int(input())

for _ in range(N):
    step = int(input())
    enc_msg = input()

    # Decrypt message
    dec_msg = ""
    for i in range(len(enc_msg)):
        char_as_int = ord(enc_msg[i])
        if A_INT <= char_as_int <= Z_INT:
            new_int = char_as_int - step
            if new_int < A_INT:
                new_int += ALPHABET_LENGTH
            dec_msg += chr(new_int)
        else:
            dec_msg += enc_msg[i]

    print(dec_msg)