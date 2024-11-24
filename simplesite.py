""" Програма використовує flask та запускає веб-сервер.
При запиті на цей сервер він повертає вміст файлу index.html """
from flask import Flask, url_for, redirect
import os

def index():
    """ функція перенаправляє на URL, що відповідає файлу index.html"""
    return redirect(url_for('static', filename='index.html')) 
        # url_for з першим параметром 'static' створює URL для статичного файлу
        # redirect повертає об'єкт, який при викликі перенаправляє клієнта на вказану адресу
        # (адреса для перенаправлення вказується параметром функції redirect)
folder = os.getcwd() # запам'ятали поточну робочу папку
# Створюємо об'єкт веб-додатку:
app = Flask(__name__, static_folder=folder) # перший параметр - ім'я модуля для веб-програми,
                        # параметр з ім'ям static_folder визначає ім'я папки, що містить статичні файли
# створюємо правило для URL '/': 
app.add_url_rule('/', 'index', index)   # при отриманні GET-запиту на адресу '/' на цьому сайті
                                        # запускатиметься функція index, і її значення буде відповіддю на запит.
if __name__ == "__main__":
    # Запускаємо веб-сервер:
    app.run()

