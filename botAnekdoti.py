import telebot
from telebot import types
import random


token = "5799020567:AAHA7gIxhUu3JLbJY7z4ay0HJ7E61d_tk1Q"
bot = telebot.TeleBot(token)


def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("анекдоты")
    btn2 = types.KeyboardButton("шутки за 300")
    keyboard.add(btn1, btn2)
    return keyboard


@bot.message_handler(commands=["start"])
def main_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("начать деградацию")
    btn2 = types.KeyboardButton("about")
    keyboard.add(btn1, btn2)
    bot.send_message(
        message.chat.id, text="Привет, тут будут гениальные анекдоты и лучшие бородатые шутоки", reply_markup=keyboard)


def mainmenu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = types.KeyboardButton("дайте мне уже меню!")
    btn4 = types.KeyboardButton("назад")
    keyboard.add(btn3, btn4)
    return keyboard


def deystvia():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn5 = types.KeyboardButton("анекдоты")
    btn6 = types.KeyboardButton("шуточки за 300")
    btn7 = types.KeyboardButton("создать свой анекдот")
    btn4 = types.KeyboardButton("назад")
    keyboard.add(btn5, btn6, btn7, btn4)
    return keyboard


@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == "начать деградацию":
        bot.send_message(message.chat.id, "чего же ты хочешь?",
                         reply_markup=mainmenu())
    if message.text == "about":
        bot.send_message(
            message.chat.id, "я гений, который создал этот шедевральный бот (@NotHumanFS)")

    if message.text == "дайте мне уже меню!":
        bot.send_message(message.chat.id, "на уже свое меню",
                         reply_markup=deystvia())
    if message.text == "назад":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("начать деградацию")
        btn2 = types.KeyboardButton("about")
        keyboard.add(btn1, btn2)
        bot.send_message(
            message.chat.id, text="Привет, тут будут гениальные анекдоты и лучшие бородатые шутоки", reply_markup=keyboard)

    if message.text == "анекдоты":
        b = random.randint(1, 10)
        if b == 1:
            bot.send_message(
                message.chat.id, text="- Батюшка! Вы что пить будете, вино или водку? - И пиво, сын мой, и пиво!…", reply_markup=deystvia())
        if b == 2:
            bot.send_message(
                message.chat.id, text="Чукча зашел в трамвай: – А я на этом трамвае до конечной доеду?", reply_markup=deystvia())
        if b == 3:
            bot.send_message(
                message.chat.id, text="– Ребята, вы, откуда будете? – Мы из горлА будем…", reply_markup=deystvia())
        if b == 4:
            bot.send_message(
                message.chat.id, text="Гаишники тормозят Нового Русского и проверяют документы. – Слышь, командир, давай быстрей, там за мной твои коллеги гоняться…", reply_markup=deystvia())
        if b == 5:
            bot.send_message(
                message.chat.id, text="В Москве разрешат один раз в году переходить от одного барина к другому без QR-кода.", reply_markup=deystvia())
        if b == 6:
            bot.send_message(
                message.chat.id, text="– Привет, ты мне откуда звонишь? Номер что–то не определяется? – С домофона придурок, дверь открой, третий час стою!", reply_markup=deystvia())
        if b == 7:
            bot.send_message(
                message.chat.id, text="– Мне нравится вон тот бегун с красным шарфиком вокруг шеи… – Это не шарф – это язык.", reply_markup=deystvia())
        if b == 8:
            bot.send_message(
                message.chat.id, text="– Твоя бабушка такая веселая! Все время улыбается!– Да это ей зубной протез не того размера вставили!", reply_markup=deystvia())
        if b == 9:
            bot.send_message(
                message.chat.id, text="Катится колобок. Катится… Катится… А потом останавливается и говорит: – Что–то голова болит.", reply_markup=deystvia())
        if b == 10:
            bot.send_message(
                message.chat.id, text="– Официант, это не суп, а какая–то вода! – Не какая–то, а кипяченая!", reply_markup=deystvia())

    if message.text == "шуточки за 300":
        c = random.randint(1, 10)
        if c == 1:
            bot.send_message(
                message.chat.id, text="Жаль, что кремом от раздражения нельзя намазаться изнутри", reply_markup=deystvia())
        if c == 2:
            bot.send_message(
                message.chat.id, text="Только первая бутылка алкоголя стоит дорого. Потом цена не имеет значения...", reply_markup=deystvia())
        if c == 3:
            bot.send_message(
                message.chat.id, text="Водка была на столько паленая, что состав был сразу написан шрифтом Брайля", reply_markup=deystvia())
        if c == 4:
            bot.send_message(
                message.chat.id, text="Чтобы не сидеть без денег - я прилег", reply_markup=deystvia())
        if c == 5:
            bot.send_message(
                message.chat.id, text="Ничто так не бодрит с утра, как чашечка, вылетевшая из коленного сустава", reply_markup=deystvia())
        if c == 6:
            bot.send_message(
                message.chat.id, text="колобок повесился", reply_markup=deystvia())
        if c == 7:
            bot.send_message(
                message.chat.id, text="негр загарает", reply_markup=deystvia())
        if c == 8:
            bot.send_message(
                message.chat.id, text="ежик на танке", reply_markup=deystvia())
        if c == 9:
            bot.send_message(
                message.chat.id, text="Отец случайно проглотил флешку. Теперь его в семье так и называют - папка с файлами.", reply_markup=deystvia())
        if c == 10:
            bot.send_message(
                message.chat.id, text="- Как называется будка охранника на кладбище?- Живой уголок!", reply_markup=deystvia())


bot.polling(non_stop=True)
