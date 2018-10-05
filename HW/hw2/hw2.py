#!/usr/bin/env python
# coding: utf-8

# In[74]:


def choose_user(names):
    user = input()
    while user not in names:
        print('Данного имени нет в списке! Попробуйте еще раз:')
        user = input()
    print('Вы выбрали пользователя', user)
    return user


# In[75]:


def gh_url(user):
    url = 'https://api.github.com/users/%s/repos' % user  
    return url


# In[76]:


def load_data(url):
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    data = json.loads(text)
    return data


# In[77]:


def rep_stats(data, user):
    lang = []
    print('Вот список его репозиториев:')
    for i in data:
        print(i["name"], ': ', i["description"])
        lang.append(i["language"])
    a = set(lang)
    list(a)
    a.remove(None)
    a = ', '.join(a)
    print('Пользователь', user, 'пишет на', a, end = '.\n')
    


# In[78]:


import json
import urllib.request
names = ['elmiram', 'maryszmary', 'lizaku', 'nevmenandr', 'ancatmara', 'roctbb', 'akutuzov', 'agricolamz', 'lehkost', 'kylepjohnson', 'mikekestemont', 'demidovakatya', 'shwars', 'timgraham', 'arogozhnikov', 'jasny', 'bcongdon', 'whyisjake', 'gvanrossum']

def main(names):
    user = choose_user(names)
    url = gh_url(user)
    data = load_data(url)
    print(rep_stats(data, user))

print(main(names))
    
        
        


# In[ ]:




