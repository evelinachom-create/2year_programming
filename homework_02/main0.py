#Приклад модуль requests
#Питання: Що він виконує? НА Д/З

pip install requests #команда інсталювання модуля requests

import requests #підключення модуля requests
response = requests.get('https://api.github.com') #надсилання запиту на отримання відповіді гітхабу(на вказану адресу), отримана інформація зберігається в змінній response
print(response.status_code) #виведення відповіді сервера на запит (наприклад, 200 - успішно)