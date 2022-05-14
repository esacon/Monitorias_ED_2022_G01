import nltk
nltk.download('words')
from nltk.corpus import words

ENGLISH_WORDS = dict.fromkeys(words.words(), None)

ALFABETO = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.áéíóú?!¿¡"

def caesar_cypher(char, k):
    if char in ALFABETO:
        num = ALFABETO.find(char) + k
        if num >= len(ALFABETO):
            num -= len(ALFABETO)
        elif num < 0:
            num += len(ALFABETO)
        return ALFABETO[num]
    return char


def code_message(message, k):
    encoded_text = ""
    for char in message:
        encoded_text += caesar_cypher(char, k)
    return encoded_text


def decode_message(message):
    MAX_K = len(ALFABETO)

    for k in range(1, MAX_K + 1):
        decoded_text = ""
        for char in message:
            decoded_text += caesar_cypher(char, -k)
        if message_has_sense(decoded_text):
            print(f'k={k}.\t{decoded_text}')
            return decoded_text    
    return message


def message_has_sense(text):
    text = text.split()
    min_words = len(text)//2
    count = 0
    for word in text:
        try:
            ENGLISH_WORDS[word]
            count += 1
        except KeyError:
            continue
    return count >= min_words


def main(k=20):
    message = "Add a hidden input to your form with the class simple-file-upload. The add-on will attach to this hidden input, and return the value of the dropped file in the value parameter of the hidden input. This is the preferred method of implementation. It provides a better user experience, and allows the existing file to be previewed in the drop box UI. If no class of simple-file-upload is found, the widget will attach to existing form inputs of type file, described below."
    print('\nEl mensaje cifrado es:')
    encoded_message = code_message(message, k)
    print(encoded_message)
    print('\nEl mensaje descifrado es:')
    decoded_text = decode_message(encoded_message)
    # print(decoded_message)
    

if __name__ == '__main__':
    main(k=60)

