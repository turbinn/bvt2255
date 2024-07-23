import telebot
from telebot import types
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Токен для бота
TOKEN = '6310902050:AAHyeKrUmHXeB7rJYihhqlT269tXHR0DUr4'
bot = telebot.TeleBot(TOKEN)

# Список администраторов (tg ID)
admin_ids = [589850009]

# Список квартир
apartments = [
    {'id': 1, 'name': '1-комнатная квартира на Авиамоторной', 'description': 'Уютная 1-комнатная квартира в центре города.', 'price': '10000 руб/мес', 'type': '1-комнатная', 'photos': ['https://artproducts.ru/media/wp-content/uploads/2022/06/dizain-odnokomnatnoi-kvartiry-1-1140x700.png', 'https://my-dom.design/wp-content/uploads/2023/06/kuhnja-gostinaja-2-1.jpg']},
    {'id': 2, 'name': '1-комнатная квартира на Авиамоторной', 'description': 'Уютная 1-комнатная квартира в центре города.', 'price': '10000 руб/мес', 'type': '1-комнатная', 'photos': ['https://cdn2.divan.ru/img/v1/zZopBG2UxXbZfti4HzKRodSDgOz4w6arNZVztDXdhuY/rs:fit:1920:1440:0:0/g:ce:0:0/bg:ffffff/q:85/czM6Ly9kaXZhbi9ja2VkaXRvci93aWtpLWFydGljbGUvMjU3MC82M2M1NWIwYzg2YWUxLmpwZw.jpg', 'https://salon.ru/storage/thumbs/gallery/710/709862/5000_5000_s123.jpg']},
    {'id': 3, 'name': '1-комнатная квартира на Авиамоторной', 'description': 'Уютная 1-комнатная квартира с современной мебелью.', 'price': '15000 руб/мес', 'type': '1-комнатная', 'photos': ['https://dbo.ru/upload/big/885539_1.jpg', 'https://dbo.ru/upload/big/885539_2.jpg']},
    {'id': 4, 'name': '2-комнатная квартира на Авиамоторной', 'description': 'Обычная 2-комнатная квартира, подходящая для семьи.', 'price': '20000 руб/мес', 'type': '2-комнатная', 'photos': ['https://cdn.mskguru.ru/uploads/flats/4611/kvartry-v-4611-zhk-festivaly-park2-1606137615_5112.jpg', 'https://www.vincent-realty.ru/upload/resize_cache/iblock/715/1600_1200_0e00602c9673d0782708401ec29b5239f/9hii8ztbjbod1ewd7ve60paf8gkm83ze.jpg']},
    {'id': 5, 'name': 'Современная 2-комнатная квартира на Авиамоторной', 'description': 'Современная 2-комнатная квартира с новым ремонтом.', 'price': '24000 руб/мес', 'type': '2-комнатная', 'photos': ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOE3DpDkqpt_m_XuHPfT7UxDQwCz1-SIe2og&s', 'https://i.pinimg.com/originals/b9/dc/fd/b9dcfd440d540103509661a2f1487d72.jpg', 'https://dizayn-interera.moscow/images/detailed/108/1.jpg']},
    {'id': 6, 'name': 'Просторная 2-комнатная квартира с видом на парк', 'description': 'Просторная 2-комнатная квартира с видом на парк.', 'price': '25000 руб/мес', 'type': '2-комнатная', 'photos': ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDRc6pD6klzUMWELy_UZaIHoLbXdxXNaW7Sg&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGPOId7vQOlXkaurSvvFLMIFjxIukXs-pdUg&s']},
    {'id': 7, 'name': 'Современная студия на Авиамоторной', 'description': 'Современная студия с новым ремонтом.', 'price': '8000 руб/мес', 'type': 'Студия', 'photos': ['https://remont-f.ru/upload/iblock/f6a/06.jpg', 'https://remont-f.ru/upload/resize_cache/iblock/1b8/440_275_2/dizayn-interyera-3-komnatnoj-kvartiry-106-kv-m-foto-9-3866.jpg']},
    {'id': 8, 'name': 'Комфортная студия на Авиамоторной', 'description': 'Комфортная студия с евро ремонтом.', 'price': '9000 руб/мес', 'type': 'Студия', 'photos': ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMeUM4hN7nZDMPVdHrCLcIa2RxpBCCvh1GeQ&s', 'https://cdn.worldota.net/t/640x400/extranet/50/71/5071f3febbaef6c49efd22865f9f76db737d712c.jpeg']},
    {'id': 9, 'name': 'Бомбовая студия на Авиамоторной', 'description': 'Бомбовая студия с шикарным ремонтом.', 'price': '8500 руб/мес', 'type': 'Студия', 'photos': ['https://cdn.worldota.net/t/x500/extranet/be/b7/beb7716f9e04dbe7d6fb0c1f00bce994497a7000.jpeg', 'https://cdn.worldota.net/t/640x400/extranet/96/05/9605ec9fb718df5dfdf5478e953ffe2b1821388e.jpeg']}
]

# Словарь для хранения состояния пользователя
user_states = {}

# Функция для создания основного меню
def create_main_menu(is_admin=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    list_button = types.KeyboardButton('🏢 Список помещений')
    contact_button = types.KeyboardButton('📞 Контакты')
    help_button = types.KeyboardButton('ℹ Помощь')

    if is_admin:
        admin_button = types.KeyboardButton('🔧 Администрирование')
        markup.add(list_button, contact_button, help_button, admin_button)
    else:
        markup.add(list_button, contact_button, help_button)

    return markup

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    is_admin = message.from_user.id in admin_ids
    bot.send_message(message.chat.id, 'Привет! Я бот для аренды помещений. Чем могу помочь?', reply_markup=create_main_menu(is_admin))

# Команда /help
@bot.message_handler(commands=['help'])
def help(message):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Получить список команд\n"
        "/list - Показать список доступных помещений\n"
        "/contact - Получить контактную информацию"
    )
    if message.from_user.id in admin_ids:
        help_text += "\n/admin - Панель администратора"
    bot.send_message(message.chat.id, help_text, reply_markup=create_main_menu(message.from_user.id in admin_ids))

# Команда /list
@bot.message_handler(commands=['list'])
def list_rooms(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("1-комнатная", callback_data='filter_1-комнатная')
    button2 = types.InlineKeyboardButton("2-комнатная", callback_data='filter_2-комнатная')
    button3 = types.InlineKeyboardButton("Студия", callback_data='filter_Студия')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выберите тип квартиры:', reply_markup=markup)

# Команда /requests
@bot.message_handler(commands=['requests'])
def view_requests(message):
    if message.from_user.id in admin_ids:
        try:
            with open('requests.txt', 'r') as file:
                requests_text = file.read()
            bot.send_message(message.chat.id, f'Текущие заявки на аренду:\n{requests_text}', reply_markup=create_main_menu(True))
        except FileNotFoundError:
            bot.send_message(message.chat.id, 'Файл с заявками не найден.', reply_markup=create_main_menu(True))
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к просмотру заявок.", reply_markup=create_main_menu())




# Команда /admin
@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id in admin_ids:
        admin_text = (
            "Панель администратора:\n"
            "/requests - Просмотр текущих заявок на аренду\n"
            "/delete_request [id] - Удалить заявку по идентификатору"
        )
        bot.send_message(message.chat.id, admin_text, reply_markup=create_main_menu(True))
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к административной панели.", reply_markup=create_main_menu())



# Функция для создания сообщения с информацией о квартире
def create_apartment_message(apartment, index, total):
    text = (
        f"🏠 Название: {apartment['name']}\n"
        f"📋 Описание: {apartment['description']}\n"
        f"💰 Цена: {apartment['price']}\n\n"
        f"Квартира {index+1} из {total}"
    )
    return text

# Функция для отправки информации о квартире
def send_apartment(chat_id, apartments_list, index, previous_message_ids=None):
    apartment = apartments_list[index]
    total = len(apartments_list)
    message_text = create_apartment_message(apartment, index, total)
    markup = types.InlineKeyboardMarkup(row_width=2)
    prev_button = types.InlineKeyboardButton("⬅️", callback_data=f'prev_{index}_{apartment["type"]}')
    next_button = types.InlineKeyboardButton("➡️", callback_data=f'next_{index}_{apartment["type"]}')
    book_button = types.InlineKeyboardButton("📅 Забронировать", callback_data=f'book_{apartment["id"]}')
    markup.add(prev_button, next_button, book_button)

    if previous_message_ids:
        for msg_id in previous_message_ids:
            bot.delete_message(chat_id, msg_id)

    photos = apartment['photos']
    new_message_ids = []
    if photos:
        media_group = [types.InputMediaPhoto(photo) for photo in photos]
        media_messages = bot.send_media_group(chat_id, media_group)
        new_message_ids.extend([msg.message_id for msg in media_messages])

    message = bot.send_message(chat_id, message_text, reply_markup=markup)
    new_message_ids.append(message.message_id)
    
    return new_message_ids

# Обработка нажатий на inline-кнопки
@bot.callback_query_handler(func=lambda call: call.data.startswith('filter_') or call.data.startswith('prev_') or call.data.startswith('next_') or call.data.startswith('book_'))
def callback_query(call):
    data = call.data
    chat_id = call.message.chat.id

    if data.startswith('filter_'):
        filter_type = data.split('_')[1]
        filtered_apartments = [apt for apt in apartments if apt['type'] == filter_type]
        if not filtered_apartments:
            bot.send_message(chat_id, "К сожалению, нет квартир данного типа.")
            return
        user_states[chat_id] = {'index': 0, 'type': filter_type, 'message_ids': []}
        message_ids = send_apartment(chat_id, filtered_apartments, 0)
        user_states[chat_id]['message_ids'] = message_ids

    elif data.startswith('prev_') or data.startswith('next_'):
        parts = data.split('_')
        current_index = int(parts[1])
        apartment_type = parts[2]
        filtered_apartments = [apt for apt in apartments if apt['type'] == apartment_type]
        total = len(filtered_apartments)

        if data.startswith('prev_'):
            new_index = (current_index - 1) % total
        elif data.startswith('next_'):
            new_index = (current_index + 1) % total

        previous_message_ids = user_states[chat_id]['message_ids']
        message_ids = send_apartment(chat_id, filtered_apartments, new_index, previous_message_ids)
        user_states[chat_id]['index'] = new_index
        user_states[chat_id]['message_ids'] = message_ids

    elif data.startswith('book_'):
        apartment_id = int(data.split('_')[1])
        apartment = next((apt for apt in apartments if apt['id'] == apartment_id), None)
        if apartment:
            user_states[chat_id]['booking_apartment'] = apartment
            bot.send_message(chat_id, f"Вы выбрали для бронирования {apartment['name']}. Пожалуйста, укажите ваше имя:")
            bot.register_next_step_handler(call.message, get_name)

# Функция для получения имени пользователя
def get_name(message):
    chat_id = message.chat.id
    user_states[chat_id]['user_name'] = message.text
    bot.send_message(chat_id, "Укажите ваш номер телефона:")
    bot.register_next_step_handler(message, get_phone)

# Функция для получения телефона пользователя
def get_phone(message):
    chat_id = message.chat.id
    user_states[chat_id]['user_phone'] = message.text
    save_booking_request(chat_id)
    bot.send_message(chat_id, f"Спасибо! Ваша заявка принята. Наш менеджер скоро свяжется с вами для подтверждения.", reply_markup=create_main_menu())

# Функция для сохранения заявки в файл
def save_booking_request(chat_id):
    apartment = user_states[chat_id].get('booking_apartment')
    user_name = user_states[chat_id].get('user_name')
    user_phone = user_states[chat_id].get('user_phone')
    request_text = f"Квартира: {apartment['name']}\nИмя: {user_name}\nТелефон: {user_phone}\n\n"

    with open('requests.txt', 'a') as file:
        file.write(request_text)

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    is_admin = message.from_user.id in admin_ids

    if text == '🏢 список помещений':
        list_rooms(message)
    elif text == '📞 контакты':
        bot.send_message(message.chat.id, 'Контактная информация:\nТелефон: +7 123 456-78-90\nEmail: info@example.com')
    elif text == 'ℹ помощь':
        help(message)
    elif text == '🔧 администрирование' and is_admin:
        bot.send_message(message.chat.id, 'Добро пожаловать в панель администратора!')
    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понял. Используйте /help для получения списка команд.', reply_markup=create_main_menu(is_admin))

# Запуск бота
bot.polling(none_stop=True)