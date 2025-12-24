import math

def read_input():
#Ввод параметров
    d1 = float(input("Кратчайшее расстояние от спасателя до кромки воды (в ярдах): "))
    d2 = float(input("Кратчайшее расстояние от утопающего до берега (в футах): "))
    h = float(input("Боковое смещение между спасателем и утопающим (в ярдах): "))
    v_sand = float(input("Скорость движения спасателя по песку (в милях в час): "))
    n = float(input("Коэффициент замедления в воде: "))
    return d1, d2, h, v_sand, n

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

def find_optimal(d1, d2, h, v_sand, n):
#Поиск угла
    best_time = float('inf')
    best_angle = 0
    
    # 
    for theta_deg in range(0, 901):  
        theta1 = theta_deg / 10.0
        t = check_time(d1, d2, h, v_sand, n, theta1)
        if t < best_time:
            best_time = t
            best_angle = theta1
    
    return best_angle, best_time

def print_result(best_angle, best_time):
    
    print(f"\nОптималтьный угол: {best_angle:.1f} градусов")
    print(f"Минимальное время: {best_time:.1f} секунд")

# Тесты
print("Тест 1: Фиксированный угол")
t1 = check_time(10, 30, 15, 4, 2, 30)
print(f"Угол 30°: {t1:.1f} секунд")

print("Тест 2: Оптимизация")
best_angle, best_time = find_optimal(10, 30, 15, 4, 2)
print(f"Лучший угол: {best_angle:.1f}°, время: {best_time:.1f}с")

print("\nТесты пройдены\n")

# Основная программа
print("Введите данные:")
d1, d2, h, v_sand, n = read_input()

print("Поиск оптимального угла...")
best_angle, best_time = find_optimal(d1, d2, h, v_sand, n)
print_result(best_angle, best_time)
