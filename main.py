from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import hide_link
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import logging

# инициализируем токен бота
bot = Bot(token='5430858012:AAGik33h13kbnKlYJ6F9Ls-syrNdIaZrwe0')
# создаем диспатчер
dp = Dispatcher(bot)

# логгинг и дебаг
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# айди номера
my_adm_id = '675667755'
CHAT_ID = '-1001398469562'

# рабочие кнопки бота
registr_inline = InlineKeyboardButton('☑️ Зарегистрироваться', url='https://bintradeclub.net/?refcode=W8NrtKNHi2' , callback_data='registr_inline_data')
registr_inline_kb = InlineKeyboardMarkup().add(registr_inline)

send_me_id = InlineKeyboardButton('☑️ Отправить номер аккаунта', callback_data='send_me_id_data')
send_me_id_kb = InlineKeyboardMarkup().add(send_me_id)

# основной код бота
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    # первое сообщение
    await types.ChatActions.typing(1)
    await message.answer(f"🖤 Привет! Мы команда XTRADE - профессиональные трейдеры, торгующие на финансовых биржах около двух лет! \nХочешь зарабатывать быстро и много через биржу не выходя из дома? Наша команда ждет тебя!\n\n☑️ С нами ты научишься:\n\n⚫ Техническому анализу: анализ свечей и их фигур, анализ свечных паттернов, анализ уровне п/с и трендов\n\n⚫ Фундаментальному анализу: узнаешь, когда стоит торговать, а когда нет; лучшее время эксперации, анализ новостей и ситуации в мире; как ловить уверенные, мощные сигналы с опорой на новости\n\n☑️ Ты получишь: \n\n⚫ Сигналы: каждый день в нашем вип-канале ты будешь получать более 150 сигналов, которые будет давать наш фирменный алгоритм с проходимостью 85%\n\n⚫ Торгового бота-помощника: наша уникальная разработка - тебе не нужно больше анализировать самому графики! Ты сможешь просто выбирать нужные валютные пары, а бот сам будет указывать момент входа; осталось лишь повторить за ним!\n\n⚫ Дружную команду: наши участники всегда рады помогать и давать советы новичкам. Тебе никогда не станет скучно с нами!",
                         reply_markup=registr_inline_kb)
    # следующее сообщение
    await types.ChatActions.typing(3)
    await message.answer(f"{hide_link('https://i.ibb.co/TWm5wZw/schem-of-reg-1.jpg')}"
                         f"☑️ После того, как ты зарегистрировался, ты сможешь найти свой номер аккаунта \n\n⚫️ На фотографии видно, где он расположен на сайте! \n\n🖤 Отправь мне номер твоего аккаунта, а я проверю, правильно ли ты прошел регистрацию!",
                         parse_mode='HTML', reply_markup=send_me_id_kb)

# блок помощь
@dp.message_handler(commands=['help'])
async def help(mes: types.Message):
    await mes.answer(f'{hide_link("https://i.ibb.co/4T9kpXg/help-1.jpg")}'
        f'❔Есть какие-либо вопросы? Не смог разобраться с чем-то? \n\n❕Обратись к администратору проекта: @blllamyyy',
                     parse_mode='HTML')

@dp.message_handler(commands=['information'])
async def information(mes: types.Message):
    await mes.answer(f'{hide_link("https://i.ibb.co/d0Ksy7v/information-1.jpg")}'
        f'☑️ XTRADE - это проект, нацеленный на заработок денег путём торговли на финансовых биржах\n\n❔Чем мы занимаемся: \n\n⚫️ Зарабатываем деньги: проводим технический и фундаментвльный анализ, выстраиваем страдегию торговли и получаем свою прибыль!\n\n🖤 Обучаем: для всех, кому интересна тема заработка, торговли и инвестиций, мы создаем обучающий контент, который затрагивает все, даже самы мелкие детали трейдинга\n\n⚫ Пишем софт: наши программисты каждый день совершенствуют наш оригинальный алгоритм торговли, который помогает в торговле на финансовом рынке, а так же ведут канал по отслеживанию важных экономических новостей\n\n🖤 Делимся результатами: мы всегда рады поделиться с вами нашими успехами и неудачами на финансовом рынке, так же, как и наши подписчики!',
                     parse_mode='HTML')

@dp.message_handler(commands=['faq'])
async def faq(mes: types.Message):
    await mes.answer('❔Возникли вопросы?\n\n❕Мы создали статью специально для вас, где вы сможете найти ответы на 90% возможных вопросов: https://teletype.in/@blllamyyy/faq')

# обработчик кнопки "Отправить номер аккаунта"
@dp.callback_query_handler(text='send_me_id_data')
async def send_me_id_message(call: types.CallbackQuery):
    await types.ChatActions.typing(1)

    # сообщение с номером
    await call.message.answer(f"{hide_link('https://i.ibb.co/zrcgGhK/send-acc-number.jpg')}"
                              f"☑️ Отправь мне свой номер аккаунта!\n\n⚫️ Для примера: '91630632\n\n❕Номер аккаунта должен состоять только из цифр!'",
                              parse_mode='HTML')

# обработчик полученного сообщения
@dp.message_handler()
async def check_number(msg: types.Message):
    message_text = msg.text
    user_id = msg.from_user.id
    if 'A' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'B' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'C' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'D' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'E' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'F' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'G' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'H' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'I' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'J' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'K' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'L' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'M' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'N' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'O' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'P' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Q' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'R' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'S' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'T' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'U' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'V' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'W' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'X' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Y' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Z' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'a' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'b' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'c' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'd' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'e' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'f' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'g' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'h' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'i' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'j' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'k' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'l' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'm' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'n' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'o' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'p' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'q' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'r' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 's' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 't' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'u' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'v' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'w' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'x' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'y' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'z' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    # русские
    elif 'А' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Б' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'В' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Г' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Д' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Е' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Ё' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Ж' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'З' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'И' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Й' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'К' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Л' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'М' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Н' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'О' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'П' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Р' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'С' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Т' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'У' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Ф' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Х' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Ц' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Ч' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Ш' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Щ' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Ъ' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Ы' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Ь' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Э' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Ю' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'Я' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'а' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'б' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'в' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'г' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'д' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'е' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'ё' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'ж' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'з' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'и' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'й' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'к' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'л' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'м' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'н' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'о' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'п' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'р' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'с' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'т' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'у' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'ф' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'х' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'ц' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'ч' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'ш' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'щ' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'ъ' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'ы' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'ь' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'э' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'ю' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    elif 'я' in message_text:
        await msg.answer('❕Номер аккаунта должен состоять только из цифр!')
    else:
        await msg.answer(f"☑️ А теперь финальная часть!\n\n❕Для того, чтобы попасть в наш закрытый вип-канал, пополни свой баланс на сайте нашего брокера на сумму от 1.000 ₽\n\n🖤 После этого ты получишь:\n\n⚫️ Более 100 сигналов каждый день с проходимостью от 85%\n\n⚫️ Эксклюзивные обучающие уроки\n\n⚫️ Бота-помощника и многое многое другое!")
        await types.ChatActions.typing(1)
        await msg.answer(f"{hide_link('https://i.ibb.co/fvzYNj7/acc-on-review.jpg')}"
                        f"☑️ Если ты сделал все правильно, то осталось лишь только подождать!\n\n❕Проверка аккаунта занимает не более 3 часов\n\n🖤 Все шаги выполнены? Мы напишем тебе в личные сообщения и добавим в наш вип-канал, где ты найдешь все нужные материалы и инструменты, чтобы начать строить жизнь так, как ты всегда мечтал!\n\n✔️ Возникли вопросы? Обращайся к нашему администратору: @blllamyyy",
                        parse_mode='HTML')
        # пересылает данные в чат на проверку
        await bot.send_message(CHAT_ID, '☑️ Имя пользователя:    {user}'.format(user=msg.from_user.full_name) + '\n☑️ Имя пользователя:    @{username}'.format(username=msg.from_user.username) + '\n☑️ ID Пользователя:    {id}'.format(id=msg.from_user.id) + '\n☑️ Номер аккаунта:    ' + msg.text + '\n\n⚫️ Обязательно к проверке')

# функция пересылки

# функция цикла работы бота

async def on_startup(dp):
    await bot.send_message(CHAT_ID, 'Бот начал работу')
    print("Бот запущен")

async def on_shutdown(dp):
    await bot.send_message(CHAT_ID, "Бот закончил работу")
    print("Бот закончил работу")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)