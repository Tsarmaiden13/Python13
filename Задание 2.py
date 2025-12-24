# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 14:31:20 2025

@author: Olga
"""

import math

def read_input():
#Ввод параметров
    d1 = float(input("Кратчайшее расстояние от спасателя до кромки воды (в ярдах): "))
    d2 = float(input("Кратчайшее расстояние от утопающего до берега (в футах): "))
    h = float(input("Боковое смещение между спасателем и утопающим (в ярдах): "))
    v_sand = float(input("Скорость движения спасателя по песку (в милях в час): "))
    n = float(input("Коэффициент замедления в воде: "))
    theta1 = float(input("Направление движения спасателя по песку (в градусах): "))
    return d1, d2, h, v_sand, n, theta1

def check_time(d1, d2, h, v_sand, n, theta1):
    yard_foot = 3.0
    mph_fps = 5280.0 / 3600.0

    d1_ft = d1 * yard_foot
    h_ft = h * yard_foot
    d2_ft = d2

    v_sand_fps = v_sand * mph_fps

    theta = math.radians(theta1)
    x = d1_ft * math.tan(theta)

    L1 = math.sqrt(x**2 + d1_ft**2)
    L2 = math.sqrt((h_ft - x)**2 + d2_ft**2)

    t = (L1 + n * L2) / v_sand_fps
    return t

def print_result(t):
    print(f"Время t = {t:.1f} секунд")

# Тест
print("Тест 1: Время")
t1 = check_time(10, 30, 15, 4, 2, 30)
print(f"Результат: {t1:.1f} секунд")

print("Тест 2: Замедление")
t_fast = check_time(10, 30, 15, 4, 1.5, 30)
t_slow = check_time(10, 30, 15, 4, 3.0, 30)
print(f"Быстрое: {t_fast:.1f}, Медленное: {t_slow:.1f}")


print("\nТесты пройдены\n")

# 
print("Введите данные:")
d1, d2, h, v_sand, n, theta1 = read_input()
t = check_time(d1, d2, h, v_sand, n, theta1)
print_result(t)
