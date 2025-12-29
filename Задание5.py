def read_grid(filename):
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    w, h = map(int, lines[0].strip().split())
    grid_data = []
    for line in lines[1:]:
        row = [int(c) for c in line.strip() if c in '01']
        if row:
            grid_data.extend(row)
    grid = []
    for i in range(h):
        row = grid_data[i*w:(i+1)*w]
        grid.append(row[:])
    return w, h, grid

def count_neighbors(grid, x, y, width, height):
    
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % width, (y + dy) % height
            count += grid[ny][nx]
    return count

def next_generation(grid, width, height):
    
    new_grid = [[0] * width for _ in range(height)]
    for y in range(height):
        for x in range(width):
            neighbors = count_neighbors(grid, x, y, width, height)
            cell = grid[y][x]
            if cell == 1:
                if neighbors == 2 or neighbors == 3:
                    new_grid[y][x] = 1
            else:
                if neighbors == 3:
                    new_grid[y][x] = 1
    return new_grid

def print_grid(grid):
    
    for row in grid:
        print(''.join(map(str, row)))

def main():
    input_file = "input.txt"
    steps = 10
    

    
    try:
        width, height, grid = read_grid(input_file)
        print(f"\nПоле {width}x{height}")
        print("Начало:")
        print_grid(grid)
        
        for step in range(1, steps + 1):
            print(f"\nШаг {step}/{steps}:")
            new_grid = next_generation(grid, width, height)
            print_grid(new_grid)
            grid = new_grid
        
       
        
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
