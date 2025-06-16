from collections import deque

class Player:
    """Класс, представляющий игрока"""
    def __init__(self, cards):
        self.deck = deque(cards) # создаем очередь из списка карт

    def has_cards(self):
        """метод has_cards определяет есть ли у игрока карты в колоде """
        return bool(self.deck) # возвращает False, если колода пуста, иначе True

    def draw_card(self):
        """метод draw_card позволяет игроку вытянуть карту из колоды"""
        return self.deck.popleft() # удаляет и возвращает карту из начала колоды (левого конца deque)

    def add_cards(self, first_card, second_card):
        """метод add_cards добавляет две карты в конец колоды."""
        self.deck.append(first_card) # сначала добавляет 1 карту в правый конец очереди
        self.deck.append(second_card) # затем 2 карту - карту проигравшего игрока

class Game:
    """Класс, представляющий игру"""
    def __init__(self, p1_cards, p2_cards):
        self.player1 = Player(p1_cards)
        self.player2 = Player(p2_cards)

    def play(self):
        """метод play запускает игру """
        max_rounds = 10**6
        for round_num in range(1, max_rounds + 1): # имитация раундов
            if not self.player1.has_cards(): # если колода 1 игрока пуста
                return f"second {round_num - 1}" # объявляем 2 игрока победителем, указывая раунд
            if not self.player2.has_cards(): # аналогично со вторым игроком
                return f"first {round_num - 1}"

            card1 = self.player1.draw_card() # 1 игрок вытягивает карту
            card2 = self.player2.draw_card() # 2 игрок вытягивает карту

            if self.card1_wins(card1, card2): # проверка на выигрыш 1 игрока
                self.player1.add_cards(card1, card2) # добавляем 2 карты в колоду 1 игроку
            else:
                self.player2.add_cards(card1, card2) # иначе добавляем 2 карты 2 игроку

        return "botva" # в случае достижения max_rounds, возвращаем botva

    def card1_wins(self, c1, c2):
        """метод card1_wins определяет выиграет ли 1 игрок раунд"""
        return (c1 == 0 and c2 == 9) or (c1 > c2 and not (c1 == 9 and c2 == 0))
        # случаи когда 1 игрок выигрывает:
        # карта1 = 0, карта2 = 9
        # или карта1 > карты2, но карта1 не равна 9, а карта2 не равна 0

def Proverka1(spis1):
    """функция проверяет правильность введения номеров карт 1 игрока"""
    spis_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 4
    while i <= 4 and i != -1: # i = 4, уменьшаем i в конце цикла для прохода по списку
        if len(spis1) != 5 or (spis1[i] not in spis_numbers): # если есть ошибка в длине или в символе
            print('Ошибка в 1 вводе. Попытайтесь ввести снова. Пример ввода: 1 2 3 4 5 ')
            spis1 = input('Введите любые 5 номеров 5 карт 1 игрока через пробел:').split()
            i = 5 # i = 5, начнем проверку нового ввода
        i -= 1
    return spis1

def Proverka2(spis2):
    """функция проверяет правильность введения номеров карт 2 игрока"""
    spis_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    j = 4
    while 0 <= j <= 4: # j = 4, уменьшаем j в конце цикла для прохода по списку
        if len(spis2) != 5 or (spis2[j] not in spis_numbers): # если есть ошибка в длине или в символе
            print('Ошибка во 2 вводе. Попытайтесь ввести снова. Пример ввода: 1 2 3 4 5 ')
            spis2 = input('Введите любые 5 номеров 5 карт 2 игрока через пробел:').split()
            j = 5 # j = 5, начнем проверку нового ввода
        j -= 1
    return spis2

print('Игра "Пьяница" запущена, в игре участвует 10 карт, имеющих значение от 0 до 9. Количество раундов ограничено.')
print('Значение вывода: second (номер раунда) - выиграл 2 игрок (в каком-то раунде), first - выиграл 1 игрок (в каком-то раунде), botva - количество раундов было превышено\n')
p1_input = input('Введите любые 5 номеров 5 карт 1 игрока через пробел:').split()
p2_input = input('Введите любые 5 номеров 5 карт 2 игрока через пробел:').split()


p1_input = Proverka1(p1_input) # проверяем ввод 1 и 2 колоды
p2_input = Proverka2(p2_input)
print('Колода 1 игрока:', *p1_input)
print('Колода 2 игрока:', *p2_input)


p1_cards = list(map(int, p1_input))
p2_cards = list(map(int, p2_input))

game = Game(p1_cards, p2_cards)
result = game.play()
print(result)