# TODO Написать 3 класса с документацией и аннотацией типов

class Watch:
    def __init__(self, color: str, number_of_hands, serial_numb: str):
        if not isinstance(color, str):
            raise TypeError('Название цвета str')
        self.color = color
        if number_of_hands <= 0:
            raise TypeError('Должно быть хотя бы 2 стрелки')
        self.number_of_hands = number_of_hands
        if not isinstance(serial_numb, str):
            raise TypeError('Номер str')
        self.serial_numb = serial_numb
    def broken(self):
        print('Часы неисправны')
        self.health = 0

class Cat:
    def __init__(self, nickname: str, sleep_hours: int, body_temperature):
        if not isinstance(nickname, str):
            raise TypeError('Название авиа компании должено быть типа str')
        self.nickname = nickname
        if not sleep_hours > 16:
            raise ValueError('Кошки проводят во сне от 16 часов в сутки')
        self.sleep_hours = sleep_hours
        if body_temperature < 37:
            raise ValueError('Температура тела у кошек должна быть более 37 градусов')
        self.body_temperature = body_temperature

class Essay:
    def __init__(self, number_of_words: int, heading: str):
        if not isinstance(number_of_words, int):
            raise TypeError('Количество слов должно быть числом')
        if number_of_words <= 0:
            raise ValueError('Сочинение должно содержать слова')
        self.number_of_words = number_of_words
        if not isinstance(heading, str):
            raise TypeError('Название str')
        self.heading = heading

if __name__ == "__main__":
    Swissmade_Golden_Lady = Watch('Золотой', 3, 'YLG150G')
    Swissmade_Purple_Time = Watch('Фиолетовый', 2, 'SS08V103')
    Pumpkin = Cat('Тыква', 20, 38)
    Essay_1 = Essay(250, 'Как я провел лето')
    import doctest
    doctest.testmod()
    pass

