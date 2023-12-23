import telebot
from telebot import types
import urllib.request
import json
import urllib3

token ='6807787409:AAG6wHesGtME5HgOqbYogbB_iDLVJdXm3Tc'
owner = 730113571
tuporezi = -4083361557
pinaem = -4078557325
sro4no = -4077337250
sheluha = -4058542048
usernames = ["ZhAlexiy"]

vanish = "Здравствуйте, мы команда \"STUDY HELPER\", которая своей целью ставит помощь студентам различных " \
         "ВУЗов по абсолютно разным дисциплинам. Члены нашей команды имеют большой опыт подобной работы за плечами, " \
         "а многочисленные благодарности от клиентов только подтверждают высокое качество нашей работы. Обратившись к " \
         "нам за помощью, Вы гарантированно получаете быстро и качественно выполненную работу на условиях полной " \
         "анонимности.\nЖелаем Вам приятного использования бота!С помощью команды /start Вы можете:\nА) " \
         "При регистрации в первый раз выбрать язык бота\nB) Если язык уже был выбран, поменять его на " \
         "противоположный\nПрислать задание для выполнения можно, используя команду /task. Вам будет необходимо " \
         "указать ваше учебное заведение, предмет, по которому необходимо выполнить задание, срок в который его будет " \
         "необходимо выполнить и само задание (в виде фото/текста и т.п.)\nУзнать цену выполнения задания можно будет " \
         "через команду /price\nОплата работы производится через команду /pay "
kick = "Hello, we are the 'STUDY HELPER' team which purpose is to help students from various " \
       "universities with absolutely different disciplines. Members of our team have a huge experience of completing " \
       "such a job and numerous gratitudes from the clients just confirm high quality of our job. If you ask us for a " \
       "help, you will be guaranteed to recieve fast and qualitative done job on full anonymity. We wish you a " \
       "pleasant usage of the bot!With the command /start you can:\nA) Choose the bot language " \
       "during the registration for the first time\nB) Switch the language if it has already been chosen\nYou can " \
       "send your task by using tge command /task. You will have to fill in your university name, the subject, " \
       "which task will be have to be done, deadline of it and the task itself (by photo/text, etc.)\nYou would find " \
       "out the price fot the completion of the task by using the /price command\nAll payments are made by using the " \
       "/pay command "
instruction = "С помощью команды /start Вы можете:\nА) " \
              "При регистрации в первый раз выбрать язык бота\nB) Если язык уже был выбран, поменять его на " \
              "противоположный\nПрислать задание для выполнения можно, используя команду /task. Вам будет необходимо " \
              "указать ваше учебное заведение, предмет, по которому необходимо выполнить задание, срок в который его будет " \
              "необходимо выполнить и само задание (в виде фото/текста и т.п.)\nУзнать цену выполнения задания можно будет " \
              "через команду /price\nОплата работы производится через команду /pay "
engstruction = "With the command /start you can:\nA) Choose the bot language " \
               "during the registration for the first time\nB) Switch the language if it has already been chosen\n\nYou can " \
               "send your task by using tge command /task. You will have to fill in your university name, the subject, " \
               "which task will be have to be done, deadline of it and the task itself (by photo/text, etc.)\n\nYou would find " \
               "out the price fot the completion of the task by using the /price command\nAll payments are made by using the " \
               "/pay command "

url = f"https://api.telegram.org/bot{token}/"
bot = telebot.TeleBot(token)
data = {}
ext = 'Если Вы хотите отменить зяавку и выйти в главное меню, напишите /exit'
engext = "If you want to cancel the request and exit to the main menu, type /exit"


def users_in(file_name, users):
    with open(file_name, 'w') as f:
        f.write(json.dumps(users))
'''
### Описание
Эта функция используется для записи данных о пользователях в файл в формате JSON.
### Путь
`POST /users_in`
### Параметры
- `file_name` (обязательный) - Имя файла, в который нужно записать данные о пользователях (строка)
- `users` (обязательный) - Данные о пользователях в формате JSON
### Ответ
Возвращает статус операции - успешно или с ошибкой.
#### Пример запроса
```
POST /users_in
{
  "file_name": "users.json",
  "users": [
    {
      "id": 1,
      "name": "John"
    },
    {
      "id": 2,
      "name": "Jane"
    }
  ]
}
```

#### Пример ответа
```json
{
  "status": "success"
}
### Пример использования
```python
import requests

data = {
    "file_name": "users.json",
    "users": [
        {
            "id": 1,
            "name": "John"
        },
        {
            "id": 2,
            "name": "Jane"
        }
    ]
}
'''
def users_out(file_name):
    with open(file_name, 'r') as f:
        users = json.loads(str(f.read()))
        return users

'''
## users_out
### Описание
Эта функция используется для считывания данных о пользователях из JSON файла.
### Путь
`GET /users_out`
### Параметры
- `file_name` (обязательный) - Имя файла, из которого нужно считать данные о пользователях (строка)
### Ответ
Возвращает данные о пользователях в формате JSON.
#### Пример запроса
```
GET /users_out?file_name=users.json
```

#### Пример ответа
```json
{
  "users": [
    {
      "id": 1,
      "name": "John"
    },
    {
      "id": 2,
      "name": "Jane"
    }
  ]
}
'''

@bot.message_handler(commands=['start'])
def welcome_start(message):
    """
  ## welcome_start

### Описание
Эта функция приветствует пользователя и предлагает выбрать язык бота.

### Путь
`GET /start`

### Параметры
Отсутствуют

### Ответ
Возвращает сообщение с предложением выбрать язык бота.

#### Пример запроса
GET /start
#### Пример ответа
Привет, <имя пользователя>! Выберите язык бота:
- ENGLISH
- РУССКИЙ

        """
    if not IsBaned(message):
        users = users_out('users.json')
        if message.chat.id not in users[0]:
            bot.send_message(message.chat.id, kick)
            bot.send_message(message.chat.id, vanish)
            users[0].append(message.chat.id)
            user = {}
            user['username'] = message.from_user.username
            users.append(user)
            bot.send_message(sheluha,
                             'Привет,хозяин! ' + str(
                                 message.from_user.first_name) + ' использовал команду /start')
            users_in('users.json', users)
            keyboard = types.InlineKeyboardMarkup()
            key_eng = types.InlineKeyboardButton(text='ENGLISH',
                                                 callback_data='eng')
            keyboard.add(key_eng)
            key_rus = types.InlineKeyboardButton(text='РУССКИЙ',
                                                 callback_data='rus')
            keyboard.add(key_rus)
            bot.send_message(message.from_user.id,
                             text=" Привет/Hi\n Выберите язык бота/Choose the language of the bot:",
                             reply_markup=keyboard)
            users_in('users.json', users)
        else:
            if 'rus' in users[users[0].index(message.chat.id) + 2].values():
                keyboard = types.InlineKeyboardMarkup()
                key_eng = types.InlineKeyboardButton(text='YES',
                                                     callback_data='eng')
                keyboard.add(key_eng)
                key_rus = types.InlineKeyboardButton(text='NO', callback_data='rus')
                keyboard.add(key_rus)
                bot.send_message(message.from_user.id,
                                 text="Вы хотите поменять язык бота на английский?",
                                 reply_markup=keyboard)
            else:
                keyboard = types.InlineKeyboardMarkup()
                key_eng = types.InlineKeyboardButton(text='YES',
                                                     callback_data='rus')
                keyboard.add(key_eng)
                key_rus = types.InlineKeyboardButton(text='NO', callback_data='eng')
                keyboard.add(key_rus)
                bot.send_message(message.from_user.id,
                                 text="Do you want to switch the language of the bot to Russian?",
                                 reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    """## callback_worker

### Описание
Эта функция обрабатывает действия пользователя, связанные с выбором языка бота и другими действиями.
### Путь
`POST /callback_worker`
### Параметры
- `call` (обязательный) - Данные о вызове
### Ответ
Возвращает сообщение об успешном выполнении запроса.
"""
    users = users_out('users.json')
    if call.data == "eng":
        users[users[0].index(call.message.chat.id) + 2]['lng'] = 'eng'
        bot.send_message(call.message.chat.id, "You've chosen the English language")
    elif call.data == "rus":
        users[users[0].index(call.message.chat.id) + 2]['lng'] = 'rus'
        bot.send_message(call.message.chat.id, 'Вы выбрали русский язык')
    users_in('users.json', users)
    if call.data == "yes":
        if 'срочно' in data[str(call.message.chat.id)][3].lower() \
                or "immediately" in data[str(call.message.chat.id)][3].lower():
            bot.forward_message(sro4no, call.message.chat.id,
                                data[str(call.message.chat.id)][4])
            bot.send_message(sro4no,
                             f'  ID: {data[str(call.message.chat.id)][0]}\n ВУЗ: {data[str(call.message.chat.id)][1]}\n'
                             f' Предмет: {data[str(call.message.chat.id)][2]}\n'
                             f' Срок:{data[str(call.message.chat.id)][3]}\n ')
        else:
            bot.forward_message(pinaem, call.message.chat.id,
                                data[str(call.message.chat.id)][4])
            bot.send_message(pinaem,
                             f'  ID: {data[str(call.message.chat.id)][0]}\n ВУЗ: {data[str(call.message.chat.id)][1]}\n'
                             f' Предмет: {data[str(call.message.chat.id)][2]}\n'
                             f' Срок:{data[str(call.message.chat.id)][3]}\n ')
        bot.send_message(call.message.chat.id,
                         "Ваш запрос был успешно отправлен. В ближайшее время вы получите информацию по цене и сроку выполнения задания")
    elif call.data == "no":
        if users[users[0].index(call.message.chat.id) + 2]['lng'] == 'rus':
            bot.send_message(call.message.chat.id,
                             ' Какой пункт заявки необходимо исправить?\n 1 - ВУЗ\n 2 - Предмет\n 3 - Срок\n 4 - Задание')
        else:
            bot.send_message(call.message.chat.id,
                             " Which section of the request is have to be changed?\n 1 - University name\n 2 - Subject\n 3 - Deadline\n 4 - Task")
        bot.register_next_step_handler(call.message, correct)


@bot.message_handler(commands=['help'])
def welcome_help(message):
    """## welcome_help

### Описание
Эта функция отображает справочную информацию для пользователя.

### Путь
`GET /help`

### Параметры
Отсутствуют

### Ответ
Возвращает справочную информацию.
"""
    if not IsBaned(message):
        users = users_out('users.json')
        if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
            bot.send_message(message.chat.id, instruction)
        else:
            bot.send_message(message.chat.id, engstruction)
        bot.send_message(sheluha,
                         'Привет, хозяин! ' + str(
                             message.from_user.first_name) + ' использовал команду /help')


@bot.message_handler(commands=['pay'])
def pay(message):
    """
    ## pay

### Описание
Эта функция предоставляет информацию о способе оплаты услуг.

### Путь
`GET /pay`

### Параметры
Отсутствуют

### Ответ
Возвращает информацию о способе оплаты.

"""
    if not IsBaned(message):
        users = users_out('users.json')
        if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
            bot.send_message(message.chat.id,
                             "Наша помощь, конечно, не бесплатная, для перевода денег используйте следующий номер карты:\n"
                             " . \n"
                             "Владелец: ")
        else:
            bot.send_message(message.chat.id,
                             "Ouf help, of course, is not free, for transferring the money use the following card number:\n"
                             ". \n"
                             "Card holder: . ")
        bot.send_message(sheluha,
                         'Привет, хозяин ! ' + str(
                             message.from_user.first_name) + ' использовал команду /pay')

@bot.message_handler(commands=["price"])
def price(message):
    """
    ## price

### Описание
Эта функция обрабатывает команду для получения информации о цене услуг.

### Путь
`GET /price`

### Параметры
Отсутствуют

### Ответ
Возвращает информацию о получении запроса и ответе в ближайшее время.
"""
    if not IsBaned(message):
        users = users_out('users.json')
        if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
            bot.send_message(message.chat.id,
                             "Ваш запрос был успешно получен. В ближайшее время мы Вам ответим")
        else:
            bot.send_message(message.chat.id,
                             "Your request has been successfully received. We will answer you in a short time")
        bot.forward_message(tuporezi, message.chat.id, message.message_id)
        bot.send_message(tuporezi, message.chat.id)


@bot.message_handler(commands=['task'])
def exercise(message):
    """## exercise

### Описание
Эта функция обрабатывает команду для отправки запроса на выполнение задания.

### Путь
`POST /exercise`

### Параметры
Отсутствуют

### Ответ
Отправляет сообщение с инструкциями.

```
"""
    if not IsBaned(message):
        users = users_out('users.json')
        bot.send_message(sheluha,
                         'Привет, хозяин! ' + str(
                             message.from_user.first_name) + ' использовал команду /task')
        if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
            bot.send_message(message.chat.id,
                             'Для того, чтобы оставить заявку на выполнение задания, необходимо сначала заполнить несколько полей\n'
                             'Введите название вашего университета (необязательно, можно поставить прочерк)\n'
                             f'{ext}')
        else:
            bot.send_message(message.chat.id,
                             'To send a reguest for completion of the task, you have to fill in a few fields at first\n'
                             'Enter the name of your university (not obligatory, you may leave a dash)\n'
                             f'{engext}')
        data[str(message.chat.id)] = []
        data[str(message.chat.id)].append(message.chat.id)
        bot.register_next_step_handler(message, university)



@bot.message_handler(commands=['send'])
def working(message):
    '''
    ## working

### Описание
Эта функция отправляет сообщение заданному получателю.

### Путь
`POST /working`

### Параметры
- `message` (обязательный) - Сообщение, которое необходимо отправить

### Ответ
Возвращает статус выполнения операции.

    :param message:
    :return:
    '''
    if message.from_user.username in usernames:
        try:
            recipient_id = '730113571'
            text = message.text.split(' ', 1)[1]  # Получаем текст сообщения после команды /send
            bot.send_message(recipient_id, text)
        except:
            bot.send_message(message.chat.id,
                             "Что-то пошло не так!", parse_mode='HTML')
    else:
        bot.send_message(message.chat.id,
                         'Вы не являетесь администратором для выполнения этой команды!')


@bot.message_handler(commands=['photo'])
def working(message):
    if message.from_user.username in usernames:
        try:
            bot.register_next_step_handler(message, sender)
        except:
            bot.send_message(message.chat.id,
                             "Что-то пошло не так!", parse_mode='HTML')
    else:
        bot.send_message(message.chat.id,
                         'Вы не являетесь администратором для выполнения этой команды!')


@bot.message_handler(content_types=["sticker", "document", "audio", "photo", "voice", "video"])
def messages(message):
    '''
# messages

### Описание
Эта функция обрабатывает различные типы медиа-сообщений, такие как стикеры, документы, аудио, фото, голосовые и видео.

### Путь
`POST /messages`

### Параметры
- `message` (обязательный) - Сообщение, которое необходимо обработать

### Ответ
Возвращает статус успешного выполнения операции.


    '''
    if not IsBaned(message):
        try:
            bot.forward_message(tuporezi, message.chat.id, message.message_id)
        except:
            bot.send_message(tuporezi,
                             'Что-то пошло не так! Бот продолжил свою работу.')


@bot.message_handler(content_types=["text"])
def messages(message):
    '''
    # messages

### Описание
Эта функция обрабатывает текстовые сообщения.

### Путь
`POST /messages`

### Параметры
- `message` (обязательный) - Текстовое сообщение, которое необходимо обработать

### Ответ
Возвращает статус успешного выполнения операции.

    '''
    if not IsBaned(message):
        print(f"{message.from_user.username} : ", message.text)
        try:
            bot.forward_message(tuporezi, message.chat.id, message.message_id)
        except:
            bot.send_message(tuporezi,
                             'Что-то пошло не так! Бот продолжил свою работу.')


def process_mind(message):
    """
# Функция Process Mind

## Описание
Эта функция используется для обработки входящих сообщений. Она проверяет, является ли отправитель сообщения пользователем с правами администратора, и если да, пересылает сообщение другому пользователю и отправляет конкретное сообщение этому пользователю. Если отправитель сообщения не является администратором, он отправляет сообщение, информирующее пользователя о том, что он не авторизован для выполнения команды.

## Параметры
- message: Объект входящего сообщения, содержащий информацию об отправителе, содержимом и чате.

## Возвращает
Эта функция не возвращает никакого значения.

## Разрешение
Пользователь, выполняющий эту функцию, должен быть администратором.
    """
    if message.from_user.username in usernames:
        try:
            text = 'Сообщение было отправлено пользователю ' + str(
                message.reply_to_message.forward_from.first_name)
            bot.send_message(message.reply_to_message.forward_from.id,
                             f"GOD: {message.text}")
            bot.send_message(tuporezi, text)
        except:
            bot.send_message(message.chat.id,
                             'Что-то пошло не так! Бот продолжил свою работу.',
                             parse_mode='HTML')
    else:
        bot.send_message(message.chat.id,
                         'Вы не являетесь администратором для выполнения этой команды!')


def IsBaned(message):
    '''
    # Функция IsBaned

## Описание
Функция IsBaned используется для проверки, заблокирован ли чат на основе предоставленного сообщения. Она извлекает список заблокированных пользователей из файла JSON и проверяет, присутствует ли идентификатор чата сообщения в списке заблокированных чатов.

## Параметры
- message: Объект сообщения, используемый для определения идентификатора чата для проверки блокировки.

## Возвращаемое значение
- True: Если идентификатор чата найден в списке заблокированных чатов.
- False: Если идентификатор чата не найден в списке заблокированных чатов.
    '''
    users = users_out('users.json')
    return str(message.chat.id) in users[1]


def sender(message):
    """
    Описание:функция присылает id отправителя и пересылает его сообщение
    :param message:
    :return:
    """
    if message.from_user.username in usernames:
        try:
            text = 'Сообщение было отправлено пользователю ' + str(
                message.reply_to_message.forward_from.first_name)
            bot.send_photo(message.reply_to_message.forward_from.id,
                           open(f'{message.text}', "rb"))
            bot.send_message(tuporezi, text)
        except:
            bot.send_message(message.chat.id,
                             'Что-то пошло не так! Бот продолжил свою работу.',
                             parse_mode='HTML')
    else:
        bot.send_message(message.chat.id,
                         'Вы не являетесь администратором для выполнения этой команды!')


def university(message):
    '''
    описание:Функция принимает сообщение с названием университета
    :param message:
    :return:
    '''
    users = users_out('users.json')
    if message.text != "/exit":
        data[str(message.chat.id)].append(message.text)
        if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
            bot.send_message(message.chat.id, 'Введите предмет\n'
                                              f'{ext}')
        else:
            bot.send_message(message.chat.id, "Enter the subject\n"
                                              f"{engext}")
        bot.register_next_step_handler(message, expiration_date)
    else:
        exit(message)


def expiration_date(message):
    """
    описание:функция принимает дату для сдачи работы и при добавление слов срочно или imediatly отправляет в разные беседы
    :param message:
    :return:
    """
    users = users_out('users.json')
    if message.text != "/exit":
        data[str(message.chat.id)].append(message.text)
        if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
            bot.send_message(message.chat.id,
                             'Введите срок выполнения задания\n'
                             'Если ответ необходим в ближайшее время, напишите дату и слово СРОЧНО\n'
                             'Например, *05/10 СРОЧНО*'
                             f'{ext}')
        else:
            bot.send_message(message.chat.id, 'Enter the deadline for the task\n'
                                              'If you need the answer in a short time, write date and the word IMMEDIATELY\n'
                                              'For example, *05/10 IMMEDIATELY*'
                                              f'{engext}')
        bot.register_next_step_handler(message, task)
    else:
        exit(message)


def task(message):
    '''
    описание:функция принимает условия задания и пересылает его
    :param message:
    :return:
    '''
    users = users_out('users.json')
    if message.text != "/exit":
        data[str(message.chat.id)].append(message.text)
        if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
            bot.send_message(message.chat.id,
                             "Прикрепите условие задания\n"
                             f"{ext}")
        else:
            bot.send_message(message.chat.id,
                             "Send the task itself\n"
                             f"{engext}")
        bot.register_next_step_handler(message, ok)
    else:
        exit(message)


def ok(message):
    '''
    описание:функция пересылает заполненную форму и спрашивает,о правильности ее заполнения
    :param message:
    :return:
    '''
    users = users_out('users.json')
    if message.text != '/exit':
        if len(data[str(message.chat.id)]) == 4:
            data[str(message.chat.id)].append(message.message_id)
        if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
            bot.send_message(message.chat.id,
                             f' ВУЗ: {data[str(message.chat.id)][1]}\n Предмет: {data[str(message.chat.id)][2]}\n'
                             f' Срок:{data[str(message.chat.id)][3]}\n Задание :')
        else:
            bot.send_message(message.chat.id,
                             f' University: {data[str(message.chat.id)][1]}\n Subject: {data[str(message.chat.id)][2]}\n'
                             f' Deadline: {data[str(message.chat.id)][3]}\n Task :')
        bot.forward_message(message.chat.id, message.chat.id,
                            data[str(message.chat.id)][4])
        bot.send_message(message.chat.id, '?')
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='ДА/YES', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='НЕТ/NO', callback_data='no')
        keyboard.add(key_no)
        if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
            bot.send_message(message.from_user.id,
                             text="Заявка заполнена корректно?",
                             reply_markup=keyboard)
        else:
            bot.send_message(message.from_user.id,
                             text="Is the request filled correctly?",
                             reply_markup=keyboard)
    else:
        exit(message)


def correct(message):
    '''
    описание:функция дает выбрать в какоим пункте допущена ошибка
    :param message:
    :return:
    '''
    users = users_out('users.json')
    if message.text not in ['1', '2', '3', '4']:
        if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
            bot.send_message(message.chat.id,
                             " 1 - ВУЗ\n 2 - Предмет\n 3 - Срок\n 4 - Задание")
        else:
            bot.send_message(message.chat.id,
                             " 1 - University\n 2 - Subject\n 3 - Deadline\n 4 - Task")
        bot.register_next_step_handler(message, correct)
    else:
        if message.text == '2':
            if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
                bot.send_message(message.chat.id, 'Введите предмет\n'
                                                  f'{ext}')
            else:
                bot.send_message(message.chat.id, "Enter the subject"
                                                  f"{engext}")
            bot.register_next_step_handler(message, dol)
        elif message.text == '3':
            if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
                bot.send_message(message.chat.id, 'Введите срок выполнения задания\n'
                                                  f'{ext}')
            else:
                bot.send_message(message.chat.id, "Enter the deadline for the task"
                                                  f"{engext}")
            bot.register_next_step_handler(message, eb)
        elif message.text == '4':
            if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
                bot.send_message(message.chat.id,
                                 'Прикрепите условие задания\n'
                                 f'{ext}')
            else:
                bot.send_message(message.chat.id,
                                 "Send the task itself"
                                 f"{engext}")
            bot.register_next_step_handler(message, kon)
        elif message.text == '1':
            if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
                bot.send_message(message.chat.id, 'Введите название вашего университета\n'
                                                  f'{ext}')
            else:
                bot.send_message(message.chat.id, "Enter the name of your university\n"
                                                  f"{engext}")
            bot.register_next_step_handler(message, vegetable)


def dol(message):
    '''
    описание:дает исправить один из вариантов и переспрашивает о правильности анкеты
    :param message:
    :return:
    '''
    if message.text != "/exit":
        data[str(message.chat.id)][2] = message.text
        bot.send_message(message.chat.id, "Вы готовы проверить анкету ещё раз?\n"
                                          "Are you ready to check the request again?\n"
                                          f"{engext}")
        bot.register_next_step_handler(message, ok)
    else:
        exit(message)


def eb(message):
    '''
        описание:дает исправить один из вариантов и переспрашивает о правильности анкеты
        :param message:
        :return:
        '''
    if message.text != "/exit":
        data[str(message.chat.id)][3] = message.text
        bot.send_message(message.chat.id, "Вы готовы проверить анкету ещё раз?\n"
                                          "Are you ready to check the request again??\n"
                                          f"{engext}")
        bot.register_next_step_handler(message, ok)
    else:
        exit(message)


def kon(message):
    '''
        описание:дает исправить один из вариантов и переспрашивает о правильности анкеты
        :param message:
        :return:
        '''
    if message.text != "/exit":
        data[str(message.chat.id)][4] = message.message_id
        bot.send_message(message.chat.id, "Вы готовы проверить анкету ещё раз?\n"
                                          "Are you ready to check the request again?\n"
                                          f"{engext}")
        bot.register_next_step_handler(message, ok)
    else:
        exit(message)


def vegetable(message):
    '''
        описание:дает исправить один из вариантов и переспрашивает о правильности анкеты
        :param message:
        :return:
        '''
    if message.text != "/exit":
        data[str(message.chat.id)][1] = message.text
        bot.send_message(message.chat.id, "Вы готовы проверить анкету ещё раз?\n"
                                          "Are you ready to check the request again?\n"
                                          f"{engext}")
        bot.register_next_step_handler(message, ok)
    else:
        exit(message)


def exit(message):
    '''
    описаниме:позволяет отменять выбранную функцию
    :param message:
    :return:
    '''
    users = users_out('users.json')
    if users[users[0].index(message.chat.id) + 2]['lng'] == 'rus':
        bot.send_message(message.chat.id, "Вы отменили функцию")
    else:
        bot.send_message(message.chat.id, "You have rejected your request")


bot.send_message(sheluha, 'Скриптонит запущен! Используй, как обычно :)')

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except:
            continue
