global encr


def encryption(text, key):
    # convert the text being encrypted to list to make it iterable
    word = list(text)
    # given the pattern, if the key is 2 there will be
    # 2 words formed on the 2 rows
    # appending the 2 words gives the encrypted words
    # encrypt stores the 2 or 3 words
    encrypt = []
    # in the encrypt_list, the 2 words are joined
    # note that this is still a list
    encrypt_list = []

    # the encryption follows the pattern of skipping the indices
    # by the key
    for i in range(key):
        encrypt.append(word[i:len(word):key])
        encrypt_list += encrypt[i]

    # this converts the encrypted word which is a list to a string
    encrypt_message = "".join(str(x) for x in encrypt_list)

    return "Encrypted message: " + encrypt_message


print(encryption("Plain Text", 3))


def decryption(encr, keys):
    # converts the word to a list to make it iterable
    list_word = list(encr)
    # skip value to determine the next index
    skip = int(((len(encr)) / keys))
    decrypt = []
    decrypt_list = []

    # the encryption follows the pattern of skipping the indices
    # by the skip value determined by length of word divided by key
    for i in range(len(encr)):
        decrypt.append(list_word[i:len(list_word):skip])
        decrypt_list += decrypt[i]
        if len(decrypt_list) == len(encr):
            break

    # this converts the encrypted word which is a list to a string
    return "\nDecrypted message: " + "".join(str(x) for x in decrypt_list)

# print(decryption("PanTxli et", 2))
