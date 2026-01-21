import sys
from PIL import Image, ImageDraw

def read_grid(filename):
    
    grid = []
    with open(filename, 'r') as f:
        h, w = map(int, f.readline().split())
        for _ in range(h):
            row = [int(c) for c in f.readline().strip()]
            grid.append(row)
    return grid

def write_grid(grid, filename):
    
    with open(filename, 'w') as f:
        f.write(f"{len(grid)} {len(grid[0]) if grid else 0}\n")
        for row in grid:
            f.write(''.join(map(str, row)) + '\n')

def count_neighbors(grid, i, j):
    
    h, w = len(grid), len(grid[0])
    count = 0
    for di in [-1,0,1]:
        for dj in [-1,0,1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == 1:
                count += 1
    return count

def next_generation(grid):
    
    h, w = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            neigh = count_neighbors(grid, i, j)
            if grid[i][j] == 1:
                if neigh == 2 or neigh == 3:
                    new_grid[i][j] = 1
            else:
                if neigh == 3:
                    new_grid[i][j] = 1
    return new_grid

def save_png(grid, filename, cell_color):
    
    h, w = len(grid), len(grid[0])
    cell_size = 10
    img_size = (w * cell_size, h * cell_size)
    img = Image.new('RGB', img_size, 'black')
    draw = ImageDraw.Draw(img)
    
    r, g, b = {
        'red': (255,0,0),
        'green': (0,255,0),
        'blue': (0,0,255),
        'white': (255,255,255)
    }.get(cell_color.lower(), (255,0,0))
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                x0, y0 = j * cell_size, i * cell_size
                x1, y1 = x0 + cell_size, y0 + cell_size
                draw.rectangle([x0, y0, x1, y1], fill=(r,g,b))
    
    img.save(filename)

def main():
    
    input_file = "test.txt"      
    steps = 5                     
    cell_color = "green"          
    output_file = "result.txt"    
    
    print(f"Старт: {input_file} → {steps} шагов, цвет={cell_color}")
    
    grid = read_grid(input_file)
    write_grid(grid, output_file)
    save_png(grid, output_file.replace('.txt', '_0.png'), cell_color)
    
    for step in range(1, steps + 1):
        grid = next_generation(grid)
        out_name = output_file.replace('.txt', f'_{step}.txt')
        png_name = output_file.replace('.txt', f'_{step}.png')
        write_grid(grid, out_name)
        save_png(grid, png_name, cell_color)
        print(f"Шаг {step} выполнеен: {out_name}, {png_name}")

if __name__ == "__main__":
    main()  
