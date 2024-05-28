import random
word_list = ['ножницы', 'календарь', 'карандаш', 'картина', 'покрывало', 'местоимение', 'потолок', 'проверка']
def get_word():
    global word_list
    num = random.randrange(8)
    return word_list[num]

word = get_word()

print(word)

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте поиграем в угадайку слов!')
    print('Вы находитесь на начальной стадии игры:', display_hangman(tries))
    print('Количество попыток:', tries)
    print('Загаданное слово:', word_completion)
    while not guessed:
        what = input('Введите букву или слово целиком:   ')
        if what.isalpha():
            if len(what) == 1:
                if guessed_letters.count(what) == 1:
                    print('Вы уже вводили эту букву. Давайте попробуем еще раз:')
                    what = input('Назовите букву или слово целиком:   ')
                if guessed_letters.count(what) == 0:
                    if what in word:
                        print('Вы угадали букву!')
                        start = 0
                        m = word.count(what)
                        for i in range(m):
                            n = word.find(what, start)
                            word_completion = word_completion[:n] + what + word_completion[n + 1:]
                            start += len(word[:n + 1])
                        guessed_letters.append(what)
                        print('Продолжаем нашу игру! Загаданное слово:   ', word_completion)
                    if what not in word:
                        print('Увы, такой буквы нет в слове.')
                        guessed_letters.append(what)
                        tries -= 1
                        if tries == 0:
                            print('Оооо нет! Вы проиграли!')
                            print('Загаданное слово:', word)
                            print('А теперь вас повесят!')
                            print('Или испытать себя еще раз?')
                            otvet = input('Ответь Да или Нет?   ')
                            if otvet == 'Да' or otvet == 'да':
                                print('Ладно! Дам вам еще один шанс!')
                                play(word)
                            if otvet == 'Нет' or otvet == 'нет':
                                print('Тебе конец!')
                                print(display_hangman(tries))
                            else:
                                print('Тебе конец!')
                                print(display_hangman(tries))
                            break
                        else:
                            print('Количество попыток:', tries)
                            print('Текущее состояние игры:')
                            print(display_hangman(tries))
            if len(what) > 1:
                if guessed_words.count(what) == 1:
                    print('Вы уже вводили это слово. Давайте попробуем еще раз:')
                    what = input('Назовите букву или слово целиком:   ')
                if guessed_words.count(what) == 0:
                    if what == word:
                        print('Поздравляем, вы угадали слово! Вы победили!')
                        guessed = True
                    if what != word:
                        guessed_words.append(what)
                        print('Увы, Вы не отгадали слово.')
                        tries -=1
                        if tries == 0:
                            print('Оооо нет! Вы проиграли!')
                            print('Загаданное слово:', word)
                            print('А теперь вас повесят!')
                            print('Или испытать себя еще раз?')
                            otvet = input('Ответь Да или Нет?   ')
                            if otvet == 'Да' or otvet == 'да':
                                print('Ладно! Дам вам еще один шанс!')
                                play(word)
                            if otvet == 'Нет' or otvet == 'нет':
                                print('Тебе конец!')
                                print(display_hangman(tries))
                            else:
                                print('Тебе конец!')
                                print(display_hangman(tries))
                            break
                        else:
                            print('Количество попыток:', tries)
                            print('Текущее состояние игры:')
                            print(display_hangman(tries))
        else:
            print('Вы ввели символ, не являющийся буквой. Попробуйте еще раз.')
            what = input('Назовите букву или слово целиком:   ')
play(word)
