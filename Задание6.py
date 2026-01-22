import csv
import math

def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) >= 6:
                try:
                    zip_code = row[0]
                    lat = float(row[1])
                    lng = float(row[2])
                    city = row[3]
                    state = row[4]
                    county = row[5]
                    data.append([zip_code, lat, lng, city, state, county])
                except ValueError:
                    continue
    return data

# Поиск по ZIP
def find_zip(data, zip_code):
    for row in data:
        if row[0].upper() == zip_code.upper():
            return row
    return None

# Поиск ZIP по городу + штат
def find_by_city(data, city, state):
    zips = []
    for row in data:
        if row[3].upper() == city.upper() and row[4].upper() == state.upper():
            zips.append(row[0])
    return zips

# Расстояние
def distance(lat1, lng1, lat2, lng2):
    R = 3958.8
    lat1 = math.radians(lat1)
    lng1 = math.radians(lng1)
    lat2 = math.radians(lat2)
    lng2 = math.radians(lng2)
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return round(R * c, 2)


data = read_data("zip_codes_states.csv")

while True:
    cmd = input("Command (loc, zip, dist, end) => ").strip().lower()
    
    if cmd == "end":
        print("Done")
        break
    elif cmd == "loc":
        print("loc")
        z = input("Enter ZIP => ").strip()
        print(z)
        row = find_zip(data, z)
        if row:
            print(f"ZIP {row[0]}: {row[3]}, {row[4]}, {row[5]} county")
        else:
            print("ZIP not found")
    elif cmd == "zip":
        print("zip")
        city = input("City => ").strip()
        print(city)
        state = input("State => ").strip()
        print(state)
        zips = find_by_city(data, city, state)
        if zips:
            print(f"Zips for {city}, {state}: {', '.join(zips)}")
        else:
            print("Not found")
    elif cmd == "dist":
        print("dist")
        z1 = input("ZIP1 => ").strip()
        print(z1)
        row1 = find_zip(data, z1)
        if not row1:
            print("ZIP1 not found")
            continue
        z2 = input("ZIP2 => ").strip()
        print(z2)
        row2 = find_zip(data, z2)
        if not row2:
            print("ZIP2 not found")
            continue
        dist = distance(row1[1], row1[2], row2[1], row2[2])
        print(f"Distance: {dist} miles")
    else:
        print("Invalid command")
