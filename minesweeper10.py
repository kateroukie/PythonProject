import random


def top_left(x, y):
    if grid[x - 1][y - 1] != "B":
        grid[x - 1][y - 1] += 1


def top(x, y):
    if grid[x - 1][y] != "B":
        grid[x - 1][y] += 1


def top_right(x, y):
    if grid[x - 1][y + 1] != "B":
        grid[x - 1][y + 1] += 1


def left(x, y):
    if grid[x][y - 1] != "B":
        grid[x][y - 1] += 1


def right(x, y):
    if grid[x][y + 1] != "B":
        grid[x][y + 1] += 1


def bottom_left(x, y):
    if grid[x + 1][y - 1] != "B":
        grid[x + 1][y - 1] += 1


def bottom(x, y):
    if grid[x + 1][y] != "B":
        grid[x + 1][y] += 1


def bottom_right(x, y):
    if grid[x + 1][y + 1] != "B":
        grid[x + 1][y + 1] += 1


def start_grid(size):
    global grid
    grid = [[0 for i in range(size)] for j in range(size)]


def counting_sum(x, y):  # x,y einai sintetagmenes tis vomvas
    if x == 0:
        if y == 0:
            right(x, y)
            bottom(x, y)
            bottom_right(x, y)
        elif y == dimension - 1:
            left(x, y)
            bottom(x, y)
            bottom_left(x, y)
        else:
            left(x, y)
            right(x, y)
            bottom_left(x, y)
            bottom(x, y)
            bottom_right(x, y)
    elif x == dimension - 1:
        if y == 0:
            top(x, y)
            right(x, y)
            top_right(x, y)
        elif y == dimension - 1:
            top(x, y)
            left(x, y)
            top_left(x, y)
        else:
            top_left(x, y)
            top(x, y)
            top_right(x, y)
            left(x, y)
            right(x, y)
    elif y == 0:
        top(x, y)
        top_right(x, y)
        right(x, y)
        bottom_right(x, y)
        bottom(x, y)
    elif y == dimension - 1:
        top(x, y)
        top_left(x, y)
        left(x, y)
        bottom_left(x, y)
        bottom(x, y)
    else:
        top_left(x, y)
        top(x, y)
        top_right(x, y)
        left(x, y)
        right(x, y)
        bottom_left(x, y)
        bottom(x, y)
        bottom_right(x, y)


def bombing(num_of_bombs):
    for i in range(num_of_bombs):
        x = random.randint(1, dimension ** 2)
        while x in list_bomb:
            x = random.randint(1, (dimension ** 2))
        list_bomb.append(x)
    for elem in list_bomb:
        if elem % dimension == 0:
            grid[(elem // dimension) - 1][dimension - 1] = "B"
            counting_sum((elem // dimension) - 1, dimension - 1)
        else:
            first = elem // dimension
            second = (elem % dimension) - 1
            grid[first][second] = "B"
            counting_sum(first, second)
    for i in grid:
        print(" ".join(str(cell) for cell in i))


if __name__ == '__main__':
    grid = []
    dimension = input("Enter dimension of the matrix: ")
    while (not dimension.isnumeric()) or (int(dimension) <= 1):
        dimension = input("Enter valid dimension  of the matrix: ")
    dimension = int(dimension)
    bombs = input("Enter the number of bombs: ")
    while (not bombs.isnumeric()) or (int(bombs) > dimension ** 2) or (int(bombs) <= 1):
        bombs = input("Enter a valid number of bombs: ")
    bombs = int(bombs)
    list_bomb = list()
    start_grid(dimension)
    bombing(bombs)

