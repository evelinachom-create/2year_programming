# 2. Створити свій модуль

"""Модуль для конвертації температур між різними шкалами: Цельсій, Фаренгейт та Кельвін."""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Конвертує Цельсій у Фаренгейт."""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Конвертує Фаренгейт у Цельсій."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius: float) -> float:
    """Конвертує Цельсій у Кельвін."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin: float) -> float:
    """Конвертує Кельвін у Цельсій."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Конвертує Фаренгейт у Кельвін."""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Конвертує Кельвін у Фаренгейт."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))