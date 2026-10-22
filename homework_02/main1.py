#1. Написати програму, яка генерує пароль певної довжини
#(довжина паролю – ваша кількість символів в імені латиницею).
#Повинно бути відображення в шістнадцятковому форматі плюс
#спеціальні символи (пунктуація) та літери верхнього регістру.

import random
import string

def generate_password(length: int) -> str:
    
    if length < 3:
        raise SystemExit("Ім'я закоротке. Введіть щонайменше 3 символи, щоб вмістити всі категорії.")

    hex_chars = string.digits + "abcdef"
    punctuation_chars = string.punctuation
    uppercase_chars = string.ascii_uppercase

    all_allowed_chars = hex_chars + punctuation_chars + uppercase_chars

    password_chars = [
        random.choice(hex_chars),
        random.choice(punctuation_chars),
        random.choice(uppercase_chars)
    ]

    remaining_length = length - len(password_chars)
    for _ in range(max(0, remaining_length)):
        password_chars.append(random.choice(all_allowed_chars))
    
    random.shuffle(password_chars)
    return "".join(password_chars)

if __name__ == "__main__":
    name = input("Введіть ваше ім'я латиницею: ").strip()
    
    if not name:
        print("Ви маєте обов'язково ввести ім'я!")
    else:
        password_length = len(name)
        generated_password = generate_password(password_length)
        
        print(f"\nВведене ім'я: {name}")
        print(f"Довжина пароля (дорівнює кількості символів в імені): {password_length}")
        print(f"Згенерований пароль: {generated_password}")