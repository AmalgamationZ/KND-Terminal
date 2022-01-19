from cryptography.fernet import Fernet


KEY = b'Nk6Qk9IQNy8VPfjBS3PCFt6aMEpSiUekewJMiwRoN3A='


def decode(message):
    cipher_suite = Fernet(KEY)

    decoded_text = cipher_suite.decrypt(message)
    decoded_text = decoded_text.decode('utf-8')

    return decoded_text


def encode(message):
    cipher_suite = Fernet(KEY)

    encoded_text = cipher_suite.encrypt(bytes(message, 'utf-8'))

    return encoded_text


def encode_file(data_dict):
    args = data_dict["args"]

    file = args[1]

    with open(file, "r", encoding='utf-8') as f:
        contents = f.read()

    bytes = encode(contents)

    with open(file, "wb") as f:
        f.write(bytes)


def decode_file(data_dict):
    args = data_dict["args"]

    file = args[1]

    with open(file, "rb") as f:
        bytes = f.read()

    contents = decode(bytes)

    with open(file, "w", encoding='utf-8') as f:
        f.write(contents)


def main():
    pass


if __name__ == "__main__":
    main()