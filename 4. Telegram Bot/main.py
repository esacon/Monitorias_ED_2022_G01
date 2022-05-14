import os
import Bot as bot
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler


# Cargamos las variables de entorno al entorno de ejecución.
load_dotenv()
TOKEN = os.environ.get('TOKEN')


def main():
    # Para conectar nuestra aplicación con el bot.
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher # Manejador de solicitudes.

    # Para procesar las solicitudes del cliente, se neceita manejar los comandos.
    dp.add_handler(CommandHandler("start", bot.start))
    dp.add_handler(CommandHandler("encode", bot.encode))
    dp.add_handler(CommandHandler("decode", bot.decode))

    # Iniciar el bot.
    updater.start_polling()
    # Mantener el ciclo de ejecución hasta que ocurra una interrupción.
    updater.idle()


if __name__ == '__main__':
    main()