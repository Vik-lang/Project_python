class Node:
    """Класс представляет узел двусвязного списка"""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedDeque:
    """Класс реализует двустороннюю очередь на основе двусвязного списка"""
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0
        if iterable: # был ли передан итерируемый объект
            for item in iterable: # цикл проходит по каждому элементу в нем
                self.add_cards(item) # добавяем элемент в конец очереди

    def add_cards(self, value):
        """mетод для добавления элемента в конец очереди"""
        new_node = Node(value) # Создаем новый узел
        if self.tail is None: # пределяем не пуста ли очередь
            self.head = self.tail = new_node # новый узел становится и head, и tail очереди

        else:
            self.tail.next = new_node # Уст-m указатель next текущего последнего узла (tail) на новый узел
            new_node.prev = self.tail # Уст-m указатель prev нового узла на текущий последний узел (tail)
            self.tail = new_node # Делаем новый узел новым последним узлом (tail) дека

        self.size += 1

    def draw_card(self):
        """mетод для удаления и возврата элемента из начала очереди"""
        value = self.head.value # cохраняем значение первого элемента очереди
        self.head = self.head.next # перемещаем head на следующий узел, делая его новым первым элементом
        if self.head is None: # Проверяем, стала ли очередь пустой после удаления первого эл-та
            self.tail = None # устанавливаеm tail в None
        else:
            self.head.prev = None # Устанавливаеm указатель prev нового первого узла на None
        self.size -= 1 # Уменьшаеm размер дека на 1
        return value

    def has_cards(self):
        """Определяет пустоту очреди"""
        return self.size > 0 # возвращаем True or False

class Game:
    """Класс, представляющий игру"""
    def __init__(self, p1_cards, p2_cards):
        self.player1 = LinkedDeque(p1_cards)
        self.player2 = LinkedDeque(p2_cards)

    def play(self):
        """метод play запускает игру """
        max_rounds = 10**6 # имитация раундов
        for round_num in range(1, max_rounds + 1):
            if not self.player1.has_cards(): # если колода 1 игрока пуста
                return f"second {round_num - 1}" # объявляем 2 игрока победителем, указывая раунд

            if not self.player2.has_cards(): # аналогично со вторым игроком
                return f"first {round_num - 1}"

            card1 = self.player1.draw_card() # 1 игрок вытягивает карту
            card2 = self.player2.draw_card() # 2 игрок вытягивает карту

            if self.card1_wins(card1, card2): # проверка на выигрыш 1 игрока
                self.player1.add_cards(card1) # сначала карту 1 игрока
                self.player1.add_cards(card2) # затем 2
            else:
                self.player2.add_cards(card1)
                self.player2.add_cards(card2)

        return "botva"

    def card1_wins(self, c1, c2):
        """метод card1_wins определяет выиграет ли 1 игрок раунд"""
        return (c1 == 0 and c2 == 9) or (c1 > c2 and not (c1 == 9 and c2 == 0))
        # случаи когда 1 игрок выигрывает:
        # карта1 = 0, карта2 = 9
        # или карта1 > карты2, но карта1 не равна 9, а карта2 не равна 0


def Proverka1(spis1):
    """функция проверяет правильность введения номеров карт 1 игрока"""
    spis_numbers = [str(i) for i in range(10)]
    i = 4
    while i <= 4 and i != -1: # i = 4, уменьшаем i в конце цикла для прохода по списку
        if len(spis1) != 5 or spis1[i] not in spis_numbers: # если есть ошибка в длине или в символе
            print('Ошибка в 1 вводе. Попытайтесь ввести снова. Пример ввода: 1 2 3 4 5 ')
            spis1 = input('Введите любые 5 номеров 5 карт 1 игрока через пробел:').split()
            i = 5 # i = 5, начнем проверку нового ввода
        i -= 1
    return spis1


def Proverka2(spis2):
    """функция проверяет правильность введения номеров карт 2 игрока"""
    spis_numbers = [str(i) for i in range(10)]
    j = 4
    while 0 <= j <= 4:
        if len(spis2) != 5 or spis2[j] not in spis_numbers:
            print('Ошибка во 2 вводе. Попытайтесь ввести снова. Пример ввода: 1 2 3 4 5 ')
            spis2 = input('Введите любые 5 номеров 5 карт 2 игрока через пробел:').split()
            j = 5
        j -= 1
    return spis2


print('Игра "Пьяница" запущена, в игре участвует 10 карт, имеющих значение от 0 до 9.')
print('Программа получает на вход две строки: первая строка содержит 5 чисел, разделённых')
print('пробелами—номера карт первого игрока, вторая – аналогично 5 карт второго игрока.')
print('Карты перечислены сверху вниз, то есть каждая строка начинается с той карты,')
print('которая будет открыта первой. Количество раундов ограничено.')
print('Значение вывода: second (номер раунда) - выиграл 2 игрок (в каком-то раунде), first - выиграл 1 игрок (в каком-то раунде), botva - ничья.\n')

p1_input = input('Введите любые 5 значений 5 карт 1 игрока через пробел: ').split()
p2_input = input('Введите любые 5 значений 5 карт 2 игрока через пробел: ').split()

p1_input = Proverka1(p1_input)
p2_input = Proverka2(p2_input)

p1_card = list(map(int, p1_input))
p2_card = list(map(int, p2_input))

print('Колода 1 игрока:', *p1_card)
print('Колода 2 игрока:', *p2_card)

game = Game(p1_card, p2_card)
result = game.play()
print(result)
