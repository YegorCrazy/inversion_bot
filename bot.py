import telebot
import inverter
import os

token_file = open('/keys/' + os.environ.get('TOKEN_FILE_NAME'))
telegram_token = token_file.readline()
telegram_token = telegram_token.split('\n')[0]

bot = telebot.TeleBot(telegram_token)
print('Logged in normally')

@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.from_user.id, "Привет! Этот бот может сделать геометрическую инверсию на картинке, которую ты ему скинешь. Можешь проверить!")
    bot.send_message(message.from_user.id, "Если вам интересно узнать больше об этом преобразовании, можете прочитать о нем по ссылке: https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F_(%D0%B3%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F)")
    print('Someone logged in!')
    
@bot.message_handler(content_types=['photo'])
def invert (message):
    fileID = message.photo[-1].file_id
    photo_file = bot.get_file(fileID)
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.from_user.id, "Получил фото. Минуточку...")
    image = inverter.open_image('image.jpg')
    output = inverter.invert_image(image)
    inverter.save_image(output, 'output.jpg')
    bot.send_photo(message.from_user.id, photo=open('output.jpg', 'rb'))
    os.system('rm image.jpg output.jpg')
    print('Photo processed from ' + message.from_user.username)
    
bot.infinity_polling()
