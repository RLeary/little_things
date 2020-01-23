# prints out a grid, from a [][]def new_board():

HEIGHT = 10
WIDTH = 12
HORIZONTAL_LINE_WIDTH = WIDTH * 2 + 5
   
grid = [[None for x in range(HEIGHT)] for x in range(WIDTH)]

def render(grid):
    horizontal_line = str()
    for i in range(HORIZONTAL_LINE_WIDTH):
        horizontal_line += '-'

    lines = list()
    for x in range(HEIGHT):
        line = str()
        line_to_output = '|'
        print(horizontal_line)
        for y in range(WIDTH):
            if grid[y][x] is None:
                line_to_output += ' '
                line_to_output += '|'
            else:
                line_to_output += grid[x][y]
                line_to_output += '|'
        print(line_to_output)
    print(horizontal_line)

render(grid)