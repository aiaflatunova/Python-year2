#!/usr/bin/env python
# coding: utf-8

# In[42]:


import re
import random


# In[43]:


def begin():
    print('Выберите категорию: 1 - Цвета и оттенки, 2 - Названия цветов, 3 - Станции Москвы и МО')
    print('Введите номер выбранной категории:')
    choice = int(input())
    if choice == 1:
        filename = 'flowers.txt'
    elif choice == 2:
        filename = 'colours.txt'
    elif choice == 3:
        filename = 'stations.txt '
    else:
        print('Error')
        exit()
    return filename


        


# In[44]:


def file_open(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read()
        words = words.split('\n')
    return words
        


# In[45]:


def choose_word(words):
    word = random.choice(words)
    return word


# In[46]:


def a_mask(word):
    mask = []
    for letter in word:
        mask.append('_')
    return mask


# In[47]:


def message_tries(n):
    if n == 1:
        word_form = 'попытка'
    elif n == 2 or 3 or 4:
        word_form = 'попытки'
    elif n == 5 or 6 or 7:
        word_form = 'попыток'
    message_tries = 'У вас осталось' + n + word_form
    return message_tries


# In[48]:


def initial_message(word):
    message = 'У вас есть 9 попыток, чтобы угадать слово из' + len(word) + 'букв'
    return message


# In[49]:


def a_guess():
    print('Введите букву:')
    guess = input()
    guess.lower()
    while re.search(r'[а-яё]', guess) == None:
        print('Ошибка, пожалуйста введите букву русского алфавита')
        guess = input()
    return guess


# In[50]:


def one_try(guess, word, n):
    letters = set(word)
    if guess in letters:
        print('Так держать!')
        for i in range(len(word)):
            if guess == word[i]:
                mask.pop(i)
                mask.insert(i, guess)
    else:
        n += 1
        print('О нет!')
        print(the_hanger(n, guess)) #n - кол-во проваленных попыток
    print(mask)



# In[51]:


def the_hanger(n, guess):
    pics = [' ______ \n |/  | \n |   O \n |  /|\ \n |  / \ \n |\____', ' ______ \n |/  | \n |   O \n |  /|\ \n |  /  \n |\____', ' ______ \n |/  | \n |   O \n |  /|\ \n |    \n |\____', ' ______ \n |/  | \n |   O \n |  /| \n |    \n |\____', ' ______ \n |/  | \n |   O \n |   | \n |    \n |\____', ' ______ \n |/  | \n |   O \n |   \n |    \n |\____', ' ______ \n |/  | \n |    \n |   \n |    \n |\____', '  \n  \n |    \n |   \n |    \n |\____']
    print(pics[n])
    print(message_tries(n))
    


# In[52]:


def the_game():
    filename = begin()
    words = file_open(filename)
    word = choose_word(words)
    mask = a_mask(word)
    print(initial_message(word))
    n = 0
    while n < 9:
        guess = a_guess()
        print(one_try(guess, word, n))
        if '_' not in mask:
            print('Вы победили!')
            exit()
       


# In[53]:


print(the_game())


# In[ ]:




