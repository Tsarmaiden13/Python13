d1 = float(input("Кратчайшее расстояние от спасателя до кромки воды (в ярдах): "))
d2 = float(input("Кратчайшее расстояние от утопающего до берега (в футах): "))
h = float(input("Боковое смещение между спасателем и утопающим (в ярдах): "))
v_sand = float(input("Скорость движения спасателя по песку (в милях в час): "))
n = float(input("Коэффициент замедления в воде: "))
theta1 = float(input("Направление движения спасателя по песку (в градусах): "))

yard_foot = 3.0
mph_fps = 5280.0 / 3600.0

d1_ft = d1 * yard_foot
h_ft = h * yard_foot
d2_ft = d2

v_sand_fps = v_sand * mph_fps

import math
theta = math.radians(theta1)
x = d1_ft * math.tan(theta)

import math
L1 = math.sqrt(x**2 + d1_ft**2)

L2 = math.sqrt((h_ft - x)**2 + d2_ft**2)

t = (L1 + n * L2) / v_sand_fps
print(f"Время t = {t:.1f} секунд")
