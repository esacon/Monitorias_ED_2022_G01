import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger()


def start(update, context):
    logger.info("El usuario ha iniciado el bot.")
    name = update.message.chat.first_name
    update.message.reply_text(f'Hola, {name}. Bienvenido!')
    logger.info('Se ha saludado al usuario.')


def encode(update, context):
    logger.info("El usuario ha solicitado codificar.")
    text = update.message.text.replace('/encode', '').strip()
    k = text.split(';')[1] 
    if k:
        try:
            cifrado = cifrado_cesar(text.split(';')[0], int(k), 'cifrar')
            update.message.reply_text(f'Su mensaje cifrado es:\n{cifrado}')
        except:
            update.message.reply_text('Lo sentimos, los datos ingresados no son correctos. Por favor, intente nuevamente.')
    print(text)


def decode(update, context):
    logger.info("El usuario ha solicitado codificar.")
    text = update.message.text.replace('/decode', '').strip()
    k = text.split(';')[1] 
    if k:
        try:
            descifrado = cifrado_cesar(text.split(';')[0], int(k), 'descifrar')
            update.message.reply_text(f'Su mensaje descifrado es:\n{descifrado}')
        except:
            update.message.reply_text('Lo sentimos, los datos ingresados no son correctos. Por favor, intente nuevamente.')
    print(text)


def cifrado_cesar(message, key, mode):
    translated = ""
    LETTERS    = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.áéíóú?!¿¡"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode ==   "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    return translated


