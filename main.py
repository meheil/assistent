import os

import speech_recognition
from os import system

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def task_manager():
    """Функция открывает диспетчер задач"""
    system('taskmgr')


def control_panel():
    """Функция открывает панель управления"""
    system('start control')


def close_assistant():
    """Функция закрывает голосовой ассистент"""
    exit()


def new_tab():
    """Функция открывает новую вкладку"""
    system('start chrome https://www.google.com/')


def volume_increase():
    """Функция увеличивает громкость"""
    print('- на сколько пунктов Вы хотели бы увеличить громкость (назовите только число)')
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        num = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
    print('-', num)
    for i in range(int(num)):
        system('nircmd.exe changesysvolume 655,35')


def volume_decrease():
    """Функция уменьшает громкость"""
    print('- на сколько пунктов Вы хотели бы уменьшить громкость (назовите только число)')
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        num = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
    print('-', num)
    for i in range(int(num)):
        system('nircmd.exe changesysvolume -655,35')


def web_search():
    """Функция выполлняет поиск в интернете"""
    print('- продиктуйте запрос')
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
    print(query)
    query = query.replace(' ','+')
    system(f'start chrome https://www.google.com/search?q={query}')


def multiplication():
    """Функция умножает два числа"""
    print('- назовите первое число')
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        a = int(sr.recognize_google(audio_data=audio, language='ru-RU').lower())
    print('-', a)
    print('- назовите второе число')
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        b = int(sr.recognize_google(audio_data=audio, language='ru-RU').lower())
    print('-', b)
    print(a*b)


with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
print('-', query)

if 'диспетчер' in query or 'задач' in query or 'задачи' in query or 'задача' in query:
    task_manager()
elif 'панель' in query or 'управления' in query or 'управление' in query or 'настройки' in query:
    control_panel()
elif 'голосовой' in query or 'ассистент' in query:
    close_assistant()
elif 'вкладка' in query or 'вкладку' in query:
    new_tab()
elif 'увеличь' in query or 'увеличить' in query:
    volume_increase()
elif 'уменьшить' in query or 'уменьши' in query:
    volume_decrease()
elif 'поиск' in query or 'интернете' in query or 'интернет' in query:
    web_search()
elif 'умножить' in query or 'умножь' in query or 'числа' in query:
    multiplication()
else:
    print('команда не распозана')