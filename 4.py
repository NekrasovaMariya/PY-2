if name == "__main__":
    class _GAME:
        def __init__(self, nameGame: str, timeGame: float, limitPerson: int):
            """
            Иницилизация полей класса

            :param nameGame: Название игры
            :param timeGame: Время игры
            :param limitPerson: Кол-во пользователей

            Примеры:
            >>>  fallGuyse = _AGame(' Fall Guys ', 60, 6) # инициализация экземпляра класса
             """
            self.nameGame = nameGame  # защищенный атрибут, название игры
            self.timeGame = timeGame  # защищенный атрибут, время раунда игры
            self.person = limitPerson  # защищенный атрибут, базовое кол-во игроков

        def __str__(self) -> str:
            return f'Игра "{self.nameGame}". Время игры: {self.timeGame} мин.'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(nameGame = {self.nameGame!r}, timeGame = {self.timeGame})'

        def chekPersonCount(self, free_count_place: int) -> int:
            """
            С помощью этой функций совршается проверка кол-ва игроков.

            :param free_count_place: Кол-во свободных мест для игоков

            Примеры:
            >>> person = _GAME('fallGuse', 60, 5)
            >>> person.chekPersonCount(3)
            """
            if free_count_place <= self.limitPerson:
                raise ValueError('Ожидание игроков')
            return free_count_place = self.limitPerson


    class RUNNERGAME(_GAME):
        def __init__(self, name: str, timeGame: float, limitPerson: int, typeGame: str):
            """
            Создание и подготовка к работе объекта "RunnerGame"

            :param name: Название игры
            :param timeGame: Время игры
            :param limitPerson: Кол-во пользователей
            :param typeGame: Тип игры

            Примеры:
            >>> PencilRush = RUNNERGAME('PencilRush', 60, 5, runner) # инициализация экземпляра класса
             """
            super().__init__(name, timeGame, limitPerson)
            self.typeGame = typeGame  # защищенный атрибут, тип игры

        def __str__(self) -> str:
            return f'Игра "{self.nameGame}". Время игры: {self.timeGame} мин. Кол-во пользователей {self.limitPerson}. Тип игры {self.typeGame} '

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(nameGame = {self.nameGame!r}, timeGame = {self.timeGame}, limitPerson = {self.limitPerson}, typeGame = {self.typeGame})'


    class ARCADEGAME(_GAME):
        def __init__(self, nameGame: str, timeGame: float, limitPerson: int, currentOnline: int):
            """
            Создание и подготовка к работе объекта "ArcadeGame"

            :param name: Название игры
            :param timeGame: Время игры
            :param limitPerson: Кол-во пользователей
            :param currentOnline: Текущий онлайн

            Примеры:
            >>> ragdollThrowChallenge = ARCADEGAME('Ragdoll Throw Challenge', 60, 6, 210) # инициализация экземпляра класса
             """
            super().__init__(name, timeGame, limitPerson)
            self.currentOnline = currentOnline  # защищенный атрибут, кол-ва пользователей онлайн

        def __str__(self) -> str:
            return f'Игра "{self.nameGame}". Время игры: {self.timeGame} мин. Кол-во пользователей {self.limitPerson}. Кол-во игроков на сервере {self.currentOnline}'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(nameGame = {self.nameGame!r}, timeGame = {self.timeGame}, limitPerson = {self.limitPerson},currentOnline = {self.currentOnline}

        @staticmethod
        def checkUserEntrance() -> None:
            """
            C помошью этой функции мы проверяем подошла ли наша очередь для входа.

            Примеры: 
            >>> ragdoll_Throw_Challeng = ARCADEGAME('Ragdoll Throw Challenge', 60, 6, 210
            >>> checkUserEntrance.ragdollThrowChalleng()
           """
            ...