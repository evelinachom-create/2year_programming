import random
from colorama import Fore, Style, init
import temperature_converter_2

init(autoreset=True)

if __name__ == "__main__":
    print("Температурний порадник")

    try:
        celsius_temp = float(input("Введіть температуру в Цельсіях: "))
    except ValueError:
        print(f"{Fore.RED}Помилка! Будь ласка, введіть числове значення.")
        exit()
    
    fahrenheit = temperature_converter_2.celsius_to_fahrenheit(celsius_temp)
    kelvin = temperature_converter_2.celsius_to_kelvin(celsius_temp)
    
    if celsius_temp < 0:
        color = Fore.BLUE
        status = "Холодно"
        advice = ["Обов'язково вдягніть шапку!", "Теплі шкарпетки зараз точно не завадять!", "Може бути слизько, гуляйте обережно!"]

    elif 0 <= celsius_temp <= 15:
        color = Fore.CYAN
        status = "Прохолодно"
        advice = ["Саме час насолодитись гарячою кавою!", "Краще гуляти у водотривкому взутті.", "На сонечку точно приємніше, ніж у тіні."]

    elif 16 <= celsius_temp <= 25:
        color = Fore.GREEN
        status = "Тепло"
        advice = ["Саме час насолодитися прогулянкою околицями!", "Чудовий день для активностей на свіжому повітрі!", "Провітріть кімнату!"]

    elif 26 <= celsius_temp <= 32:
        color = Fore.YELLOW
        status = "Жарко"
        advice = ["Прихопіть кепку або капелюх", "Підтримуйте водний баланс!", "Пийте більше води!"]

    else:
        color = Fore.RED
        status = "Дуже гаряче!"
        advice = ["Можливо, сьогодні не варто виходити на вулицю?", "Обов'язково використовуйте сонцезахисний крем!", "Зовні зараз небезпечніше, ніж зазвичай!"]

    random_advice = random.choice(advice)

    print(f"Статус погоди: {color}{status}")
    print(f"У Цельсіях:   {color}{celsius_temp:.2f}°C")
    print(f"У Фаренгейтах: {color}{fahrenheit:.2f}°F")
    print(f"У Кельвінах:   {color}{kelvin:.2f} K")
    print(f"{Fore.MAGENTA} Порада дня: {random_advice}")