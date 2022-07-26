import telebot
import auth_data
import dbworker
from telebot import types


def telegram_bot():
    bot = telebot.TeleBot(auth_data.token)

    @bot.message_handler(commands=["start"])
    def cmd_start(message):
        state = dbworker.get_current_state(message.chat.id)
        if state == auth_data.States.S_1.value:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            btn1 = types.KeyboardButton("Мошково")
            btn2 = types.KeyboardButton("Яя")
            btn3 = types.KeyboardButton("Яшкино")
            btn4 = types.KeyboardButton("Юрга")
            btn5 = types.KeyboardButton("Болотное")
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.chat.id, "Я все еще жду, пока ты выберешь филиал:(Жду..", reply_markup=markup)
        elif state == auth_data.States.S_2.value:
            bot.send_message(message.chat.id, "Введите остаток товара на утро:( Жду...")
        elif state == auth_data.States.S_3.value:
            bot.send_message(message.chat.id, "Введите выручку за день:( Жду...")
        elif state == auth_data.States.S_4.value:
            bot.send_message(message.chat.id, "Введите остаток на вечер:( Жду...")
        elif state == auth_data.States.S_5.value:
            bot.send_message(message.chat.id,
                             "Введите остаток по кассе на утро:( Жду...")
        elif state == auth_data.States.S_6.value:
            bot.send_message(message.chat.id,
                             "Сумма по безналу:( Жду...")
        elif state == auth_data.States.S_7.value:
            bot.send_message(message.chat.id,
                             "Общие расходы и на что:( Жду...")
        elif state == auth_data.States.S_8.value:
            bot.send_message(message.chat.id,
                             "Остаток вечер:( Жду...")
        elif state == auth_data.States.S_9.value:
            bot.send_message(message.chat.id,
                             "Прикрепите файл:( Жду...:")
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            btn1 = types.KeyboardButton("Мошково")
            btn2 = types.KeyboardButton("Яя")
            btn3 = types.KeyboardButton("Яшкино")
            btn4 = types.KeyboardButton("Юрга")
            btn5 = types.KeyboardButton("Болотное")
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.chat.id, "Выберите Ваш отдел/филиал:", reply_markup=markup)

            dbworker.set_state(message.chat.id, auth_data.States.S_1.value)

    @bot.message_handler(commands=["reset"])
    def cmd_reset(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Мошково")
        btn2 = types.KeyboardButton("Яя")
        btn3 = types.KeyboardButton("Яшкино")
        btn4 = types.KeyboardButton("Юрга")
        btn5 = types.KeyboardButton("Болотное")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, "Повторный ввод - выберите ваш город/филиал:", reply_markup=markup)
        dbworker.set_state(message.chat.id, auth_data.States.S_1.value)

    @bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == auth_data.States.S_1.value)
    def user_s1(message):
        bot.send_message(message.chat.id, "Oстаток товара на утро:")
        dbworker.set_state(message.chat.id, auth_data.States.S_2.value)
        with open(f"file{message.chat.id}.txt", mode="w", encoding='utf-8') as f:
            f.write(f"Город/филиал: {message.text}\n")

    @bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == auth_data.States.S_2.value)
    def user_s2(message):
        bot.send_message(message.chat.id, "Выручка за день:")
        dbworker.set_state(message.chat.id, auth_data.States.S_3.value)
        with open(f"file{message.chat.id}.txt", mode="a", encoding='utf-8') as f:
            f.write(f"Oстаток товара на утро: {message.text}\n")

    @bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == auth_data.States.S_3.value)
    def user_s3(message):
        bot.send_message(message.chat.id, "Oстаток на вечер:")
        dbworker.set_state(message.chat.id, auth_data.States.S_4.value)
        with open(f"file{message.chat.id}.txt", mode="a", encoding='utf-8') as f:
            f.write(f"Выручка за день: {message.text}\n")

    @bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == auth_data.States.S_4.value)
    def user_s4(message):
        bot.send_message(message.chat.id, "Oстаток по кассе на утро:")
        dbworker.set_state(message.chat.id, auth_data.States.S_5.value)
        with open(f"file{message.chat.id}.txt", mode="a", encoding='utf-8') as f:
            f.write(f"Oстаток на вечер: {message.text}\n")

    @bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == auth_data.States.S_5.value)
    def user_s5(message):
        bot.send_message(message.chat.id, "Сумма по безналу:")
        dbworker.set_state(message.chat.id, auth_data.States.S_6.value)
        with open(f"file{message.chat.id}.txt", mode="a", encoding='utf-8') as f:
            f.write(f"Oстаток по кассе на утро: {message.text}\n")

    @bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == auth_data.States.S_6.value)
    def user_s6(message):
        bot.send_message(message.chat.id, "Общие расходы и на что:")
        dbworker.set_state(message.chat.id, auth_data.States.S_7.value)
        with open(f"file{message.chat.id}.txt", mode="a", encoding='utf-8') as f:
            f.write(f"Сумма по безналу: {message.text}\n")

    @bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == auth_data.States.S_7.value)
    def user_s7(message):
        bot.send_message(message.chat.id, "Остаток вечер:")
        dbworker.set_state(message.chat.id, auth_data.States.S_8.value)
        with open(f"file{message.chat.id}.txt", mode="a", encoding='utf-8') as f:
            f.write(f"Общие расходы и на что: {message.text}\n")

    @bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == auth_data.States.S_8.value)
    def user_s7(message):
        result_dict = {}
        bot.send_message(message.chat.id, "Прикрепите файл:")
        dbworker.set_state(message.chat.id, auth_data.States.S_9.value)
        with open(f"file{message.chat.id}.txt", mode="a", encoding='utf-8') as f:
            f.write(f"Остаток вечер: {message.text}\n")
        with open(f"file{message.chat.id}.txt", 'r', encoding='utf-8') as f:
            bot.send_message(1491905773, text=f.read())




    @bot.message_handler(content_types=["photo"],
                         func=lambda message: dbworker.get_current_state(message.chat.id) == auth_data.States.S_9.value)
    def user_sending_photo(message):
        try:
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = "photo.png"
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            with open("photo.png", 'rb') as f:
                bot.send_photo(1491905773, f.read())
        except Exception:
            bot.reply_to(message,
                         text=f"Что-то пошло не так.. Перепроверьте, пожалуйста, прикрепленный файл и прикрепите еще \
                         раз:")
        else:
            bot.send_message(message.chat.id, "Спасибо, данные сохранены. Хорошего дня! Чтобы снова начать работу,введите '/start'")
            dbworker.set_state(message.chat.id, auth_data.States.S_START.value)

    bot.polling(non_stop=True)


if __name__ == "__main__":
    telegram_bot()
