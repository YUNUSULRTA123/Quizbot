import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# Задание 2 - Импортируй нужные классы

class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    # Задание 1 - Создай геттер для получения текста вопроса
    @property
    def text(self):
        return self.__text

    def gen_markup(self):
        # Задание 3 - Создай метод для генерации Inline клавиатуры
        markup = InlineKeyboardMarkup()
        markup.row_width = len(self.options)
        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                markup.add(InlineKeyboardButton(option, callback_data='correct'))
            else:
                markup.add(InlineKeyboardButton(option, callback_data='wrong'))
        return markup

# Задание 4 - заполни список своими вопросами
quiz_questions = [
    Question("Как снять одежду с балкона", 1, "Вытащить шпилку и взять одежду", "По-человечески", "Взять телефон и снять видео"),
    Question("Кто такой Drake?", 0, "Мем", "Рэпер", "Ютубер"),
    Question("Как учить уроки?", 2, "Их не делать", "Открыть книгу и учить", "Ставить книги на стулья и учить их (Если плохо себя видут выгоняйте их из класса и ставьте 2)"),
    Question("Какой телефон самый лучший?", 2, "XIAOMI","iPhone", "Nokia", "Samsung"),
    Question("Какой из них самолёт" , 1,"Ford","BNW", "Mercedes"),
    Question("Понравилась викторина", 1,"Да👍", "Нет👎")
]