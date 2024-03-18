import telebot
from time import sleep
token = "6781458985:AAGc5-FOdcf32qob04h0Q2X0Xk5Ocwbks3k"
name = 0
main = 1
one = 0
two = 0
three = 0
four = 0
five = 0
end = 0
bot = telebot.TeleBot(token)

@bot.callback_query_handler(func=lambda callback: True)
def func(callback):
    if callback.data == 'btn_1' or callback.data == 'btn_3' or callback.data == 'btn_2' or callback.data == 'btn_4':
        func_1(callback)
    if callback.data == 'btn_5' or callback.data == 'btn_6' or callback.data == 'btn_7' or callback.data == 'btn_8' or callback.data == 'btn_9' or callback.data == 'btn_10':
        func_2(callback)
# Первая локация, начало истории*******************************************************************



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуй путник, ты готов начать своё приключение(да или нет)?')
    bot.register_next_step_handler(message, start_story)

def start_story(message):
    if message.text.lower() == 'да':
        markup = telebot.types.InlineKeyboardMarkup()
        btn_1 = telebot.types.InlineKeyboardButton('Пойти на прогулку в лес', callback_data='btn_1')
        btn_2 = telebot.types.InlineKeyboardButton('Пойти выпить', callback_data='btn_2')
        markup.add(btn_1, btn_2)
        bot.send_message(message.chat.id, 'Вы живёте в мире где каждая травинка пропитана магией, а на земле существует неизмерное количество волшебных существ. Всю жизнь вы жили в обычной деревне со своей семьёй на их фамильной земле. Сами вы как и все члены вашей семьи магией не обладаете. Семейное древо вашей семьи начиналось несколько веков назад, более ранние упоминания были утерены. Единственное что есть у вас это их семейная реликвия пренадлежащая твоему очень давнему предку - Медальон с повязкой на шее. С самого детства вам сказали чтобы ты берег его и никогда в жизни не снимал. Вы всегда помнили это и даже на ночь никогда не снимали Медальон.')
        sleep(20)
        bot.send_message(message.chat.id, 'Вы просыпаетесь рано утром. Быстро встав вы одеваетесь и спускаетесь на первый этаж. Заходя на кухню вы видите коробку посреди стола, как только вы подходите к ней появляются ваши родные и поздравляют с вашим восемнадцатилетием. Вы открываете коробку и видите там праздничный торт. Ваша семья завёт вас за стол и после чего вы весело  проводите время в кругу семьи. После этого вы выходите на улицу и думаете чем вам заняться.', reply_markup=markup)
        photo = open('images/msg1382091016-32059 (1).jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Жаль😪😪')
        bot.send_message(message.chat.id, 'Прощай')
    elif message.text == name:
        bot.send_message(message.chat.id, f'{name}')
        bot.send_message(message.chat.id, '/1 - Лес Эльфов\n'
                                          '/2 - Пустыня Орков\n'
                                          '/3 - Подземелье Нечести\n'
                                          '/4 - Гора Дварфов\n'
                                          '/5 - Пиратская Бухта\n'
                                          '/end - Забытые развалины проклятого Королевства')
@bot.callback_query_handler(func=lambda callback: True)
def func_1(callback):
    if callback.data == 'btn_1':
        markup = telebot.types.InlineKeyboardMarkup()
        btn_1 = telebot.types.InlineKeyboardButton('Вступить в драку', callback_data='btn_3')
        btn_2 = telebot.types.InlineKeyboardButton('Не рисковать', callback_data='btn_4')
        markup.add(btn_1, btn_2)
        bot.send_message(callback.message.chat.id,
                         'Идя по лесу вы думаете о своём будущем, предках, истории вашей семьи. Ваши мысли прирывает громкий крик сзади. Оборачиваясь вы видите группу людей из трёх человек. Их внешний вид выглядит '
                         'довольно таинственно. Подходя к вам они двухсмыслено спрашивают не будет ли у вас пару монет, из под плаща вы можете заметить ручку кинжала. Вы начинаете оценивать их и думать как именно вам поступить.',
                         reply_markup=markup)
    elif callback.data == 'btn_3':
        bot.send_message(callback.message.chat.id, 'Вы решаете не дожидаться пока они нападут и наносите удар первым. В ходе драки один из бандитов пытается достать кинжал, вы выбиваете кинжал из его рук но при этом не успеваете отразить удар другого бандита. Удар попадает прямо вам в грудь, не смотря на это вам удаётся перехватить инициативу в драке и в последующем победить. Побежденые бандиты быстро уносят ноги и совсем скоро скрываются из виду. Думая о том как не легко далась вам эта победа вы начинаете идти домой. Почти дойдя до дома вы вспоминаете о пропущеном ударе из-за чего в последствии вы замечаете что Медальон разбился. Прийдя домой и обработав раны вы идёте в свою комнату. Усталость сильно сказывается на вас и вы сами того не замечаю погружаетесь в сон.')
        sleep(20)
        bot.send_message(callback.message.chat.id, "Для продолжения введите ваше имя:")
        bot.register_next_step_handler(callback.message, story)
    elif callback.data == 'btn_4':
        bot.send_message(callback.message.chat.id,
                         'Оценив их вы решаете не влезать в драку и послушать их. Вы лезите в карман за имеющимися у вас деньгами как в этот момент в ваше лицо прилитает удар. Падая на землю вы можете замечаете следующий удар. У вас получается парировать его, но бандит резко бьёт вас ногой. Удар попадает вам прямо в грудь. Последнее что вы успеете заметить это летащий в вашу сторону удар ногой. Вы теряете сознание.')
        sleep(20)
        bot.send_message(callback.message.chat.id,
                         'Очнулись вы уже заполночь. Вы вспоминаете что с вами произошло. Вы начинаете осторожно вставать, вы чувствуете боль по всему телу. Вспоминая удар ногой вы поднимаете майку и замечаете разбитый Медальон на вашей шее. Сильно расстроевшись вы идетё домой думая: Правильно ли я поступил? Под расстроеные мысли вы доходите до дома. Зайдя в  дом вы быстро ложитесь в кровать и сами не замечаете как засыпаете.')
        bot.send_message(callback.message.chat.id, "Для продолжения введите ваше имя:")
        bot.register_next_step_handler(callback.message, story)
    elif callback.data == 'btn_2':
        bot.send_message(callback.message.chat.id, 'Вы решаете не напрягаться и пойти выпить в баре. Прийдя в бар вы заказываете напиток и начинаете разговор с барменом. Выпив ещё пару кружек к вам подсаживаются несколько незнакомых вам людей. У вас завязывается разговор. Хорошенько выпив вместе ваши собеседники собираются уходить, но в этот момент бармен окликивает вас и говорит о краже Медальона. Вы резко отдергиваете одного из них, в попытках вырваться вор выбрасывает Медальон и ему удаётся сбежать. Спустя пару минут вы успокоившись благодарите бармена     и собираясь уходить домой вспоминаете о выбрашеном бандитом Медальоне.')
        sleep(20)
        bot.send_message(callback.message.chat.id, "Найдя Медальон вы сильно расстраиваетесь увидя что он сильно разбит. В поникшем состоянии вы сами того не заметили как оказались дома. Не желая ни с кем разговаривать вы  ложитесь спать.")
        sleep(5)
        bot.send_message(callback.message.chat.id, "Для продолжения введите ваше имя:")
        bot.register_next_step_handler(callback.message, story)


def story(message):
    global main
    name = message.text
    bot.send_message(message.chat.id, 'Погрузившись в сон вдалеке вы видите силуэт человека. Вы медленно приближаетесь к нему, подойдя достаточно близко вы оказываетесь в неизвестном вам месте. Вы ходите по этому месту уже достаточно долго но так и не встретили того загодочного человека. Подойдя к разрушеному дому вы слышите голос позади себя. Он повествует вам о истории семьи могущественных магов, проживавших в неизвестном вам Королевстве. По ходу повествования вы узнаете о проклятьи наложенном заточившем души семьи магов и всех его жителей в руинах Королевства. Оборачиваясь на своего собеседника вы видите ту самую неизвестную фигуру из-за которой вы сюда попали. Вы смотрите на таинственную фигуру и спрашивает зачем она все это вам рассказала. Собеседник снимает капюшон, вы видите похожую на вашу родословную внешность. Вы спрашивает почему у собеседника похожая на вашу семью внешность и он рассказывает вам о прошлом вашей семьи, и что вы как и весь ваш род великий маг. Человек перед вами это ваш давний родственник. Он представляется Грэем. Говоря что у вас мало времени Грэй просит вас помочь ему, отправиться в долгое путешествие и спасти Королевство и всех его жителей от проклятья. Перед уходом Грэй сообщает вам, что теперь ваши магические способности пробудились и вы можете использовать магию.')
    sleep(30)
    bot.send_message(message.chat.id, 'Вы резко просыпаетесь. Вы обдумываете  произошедшее и вспоминаете о последних словах Грея. Вы вытягиваете руку вперёд и необычные чувства охватывают ваше тело, в вашей руке собран шар воды. Сделав резко движение вы выстреливете им пробивая стену. Вы поняли что это был не просто сон. На следующее утро вы начинаете подготовку к приключению. Собрав вещи вы прощаетесь с семьёй. Вы решили не рассказывать им правду и обусловливаете свой уход тягой путешествия и знакомства с новыми людьми. Выходя из деревни вас мучает только один вопрос. С чего бы вам начать?')
    bot.send_message(message.chat.id, '/1 - Лес Эльфов\n'
                                        '/2 - Пустыня Орков\n'
                                        '/3 - Подземелье Нечести\n'
                                        '/4 - Гора Дварфов\n'
                                        '/5 - Пиратская Бухта\n'
                                        '/end - Забытые развалины проклятого Королевства')
    main = 1
# *********************************************************************************************************************************


# Лес Эльфов***********************************************************************************************************************
@bot.message_handler(commands=['1'])
def one(message):
    global one
    if main:
        markup = telebot.types.InlineKeyboardMarkup()
        btn_1 = telebot.types.InlineKeyboardButton('Сильная мана у озера', callback_data='btn_5')
        btn_2 = telebot.types.InlineKeyboardButton('Протопная Эльфами тропинка', callback_data='btn_6')
        markup.add(btn_1, btn_2)
        photo = open('images/msg1382091016-32058.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'здесь должна быть какая-то история, но мне очень лень писать', reply_markup=markup)
        one = 1
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите /start')


@bot.callback_query_handler(func=lambda callback: True)
def func_2(callback):
    if callback.data == 'btn_5':
        markup = telebot.types.InlineKeyboardMarkup()
        btn_1 = telebot.types.InlineKeyboardButton('чето первое', callback_data='btn_7')
        btn_2 = telebot.types.InlineKeyboardButton('чето второе', callback_data='btn_8')
        markup.add(btn_1, btn_2)
        bot.send_message(callback.message.chat.id, '1', reply_markup=markup)
    elif callback.data == 'btn_6':
        markup = telebot.types.InlineKeyboardMarkup()
        btn_1 = telebot.types.InlineKeyboardButton('чето третье', callback_data='btn_9')
        btn_2 = telebot.types.InlineKeyboardButton('чето четвертое', callback_data='btn_10')
        markup.add(btn_1, btn_2)
        bot.send_message(callback.message.chat.id, '2', reply_markup=markup)
    elif callback.data == 'btn_7':
        bot.send_message(callback.message.chat.id, 'Напиши чето')
        bot.register_next_step_handler(callback.message, story_1)
    elif callback.data == 'btn_9':
        bot.send_message(callback.message.chat.id, 'Напиши чето')
        bot.register_next_step_handler(callback.message, story_1)
    elif callback.data == 'btn_8':
        bot.send_message(callback.message.chat.id, 'молчи')
    elif callback.data == 'btn_10':
        bot.send_message(callback.message.chat.id, 'тоже молчи')
def story_1(message):
    if message.text:
        bot.send_message(message.chat.id, message.text.upper())
        bot.send_message(message.chat.id, 'Что может в одно и то же время стоять и ходить, висеть и стоять, ходить и лежать?')
        bot.register_next_step_handler(message, zagadka)


def zagadka(message):
    if message.text.lower() == 'часы':
        bot.send_message(message.chat.id, 'Правильно!')
    else:
        bot.send_message(message.chat.id, ' Неправильно!')
        bot.send_message(message.chat.id, ' Вы умерли, начинайте сначала...')
        bot.register_next_step_handler(message, one)

# **********************************************************************************************************************************


# Пустыня Орков***********************************************************************************************************************
@bot.message_handler(commands=['2'])
def two(message):
    global two
    if main:
        pass
        two = 1
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите /start')
# ***************************************************************************************************************************************


# Подземелье нечести************************************************************************************************************************
@bot.message_handler(commands=['3'])
def three(message):
    global three
    if main:
        pass
        three = 1
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите /start')
# *******************************************************************************************************************************************


# Гора Дварфов******************************************************************************************************************************
@bot.message_handler(commands=['4'])
def four(message):
    global four
    if main:
        pass
        four = 1
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите /start')
# ************************************************************************************************************************************************


# Пиратская Бухта******************************************************************************************************************************
@bot.message_handler(commands=['5'])
def five(message):
    global five
    if main:
        pass
        five = 1
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите /start')
# ************************************************************************************************************************************************************************************************************************************************************


# Забытые развалины проклятого Королевства, конец истории# ************************************************************************************************************************************************
@bot.message_handler(commands=['end'])
def end(message):
    if one == 1 and two == 1 and three == 1 and four == 1 and five == 1:
        pass
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите главы: /1\n /2\n /3\n /4\n /5')
# ************************************************************************************************************************************************************************************************************************************************************


bot.infinity_polling()