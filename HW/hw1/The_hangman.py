import re
import random
def begin():
    print('Выберите категорию: 1 - Цвета и оттенки, 2 - Названия цветов, 3 - Станции метро Москвы')
    print('Введите номер выбранной категории:')
    choice = str(input())
    while re.search(r'[123]', choice) == None:
        print('Ошибка, пожалуйста введите число от 1 до 3')
        choice = str(input())
    if choice == '1':
        filename = 'flowers.txt'
    elif choice == '2':
        filename = 'colours.txt'
    elif choice == '3':
        filename = 'stations.txt '
    return filename

def file_open(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read()
        words = words.split('\n')
    return words

def choose_word(words):
    word = random.choice(words)
    word = list(word)
    return word

def a_mask(word):
    mask = []
    for letter in word:
        mask.append('_')
    return mask

def initial_message(word):
    print('У вас есть 9 попыток, чтобы угадать слово из', len(word), 'букв')

def a_guess():
    print('Введите букву:')
    guess = input()
    guess.lower()
    while re.search(r'[а-яё]', guess) == None:
        print('Ошибка, пожалуйста введите букву русского алфавита')
        guess = input()
    return guess

def one_try(guess, word, n, mask):
    letters = set(word)
    if guess in letters:
        print('Так держать!')
        for i in range(len(word)):
            if guess == word[i]:
                mask.pop(i)
                mask.insert(i, guess)
    else:
        n += 1
        tries_left = 9 - n
        print('О нет!')
        print(the_hanger(tries_left, guess)) #n - кол-во проваленных попыток
    print(mask)
    return tries_left, n, mask

def the_hanger(tries_left, guess):
    pics = [' ______ \n |/  | \n |   O \n |  /|\ \n |  / \ \n |\____', ' ______ \n |/  | \n |   O \n |  /|\ \n |  /  \n |\____', ' ______ \n |/  | \n |   O \n |  /|\ \n |    \n |\____', ' ______ \n |/  | \n |   O \n |  /| \n |    \n |\____', ' ______ \n |/  | \n |   O \n |   | \n |    \n |\____', ' ______ \n |/  | \n |   O \n |   \n |    \n |\____', ' ______ \n |/  | \n |    \n |   \n |    \n |\____', '  \n  \n |    \n |   \n |    \n |\____']
    print(pics[tries_left - 1])
    print(message_tries(tries_left))
    
def message_tries(tries_left):
    if tries_left == 1:
        word_form = 'попытка'
    elif tries_left == 2 or 3 or 4:
        word_form = 'попытки'
    elif tries_left == 5 or 6 or 7 or 8 or 9:
        word_form = 'попыток'
    print('У вас осталось', tries_left, word_form)

def the_game():
    filename = begin()
    words = file_open(filename)
    word = choose_word(words)
    mask = a_mask(word)
    print(initial_message(word))  
    n = 0
    while n < 9:
        guess = a_guess()
        print(one_try(guess, word, n, mask))
        if '_' not in mask:
            print('Вы победили!')
            exit()
        
print(the_game())
    
       
