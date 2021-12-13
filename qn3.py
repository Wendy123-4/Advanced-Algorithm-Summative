global encr


def encryption(text, key):
    # word = text
    # odd_list = []
    # even_list = []
    # enc = []
    #
    # for i in range(len(word)):
    #     if i % 2 == 0:
    #         even_list.append(word[i])
    #     else:
    #         odd_list.append(word[i])
    #
    # return even_list + odd_list

    word = list(text)
    encrypt = []
    encrypt_list = []

    for i in range(key):
        encrypt.append(word[i:len(word):key])
        encrypt_list += encrypt[i]

    encrypt_message = "".join(str(x) for x in encrypt_list)

    return "Encrypted message: " + encrypt_message


print(encryption("Plain Text", 2))


def decryption(encr, keys):
    list_word = list(encr)
    skip = int(((len(encr)) / keys))
    # if int(((len(encr)) / keys)) != ((len(encr)) / keys):
    #     skip = int(((len(encr)) / keys)) + 1
    # else:
    #     skip = int((len(encr)) / keys)

    decrypt = []
    decrypt_list = []

    for i in range(len(encr)):
        decrypt.append(list_word[i:len(list_word):skip])
        decrypt_list += decrypt[i]
        if len(decrypt_list) == len(encr):
            break

    print(skip)
    return "\nDecrypted message: " + "".join(str(x) for x in decrypt_list)


print(decryption("PanTxli et", 2))
