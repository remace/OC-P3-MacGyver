""" map generation for tests """

def create_maze(width, height):
    """function that creates a rectangle map with:
    walls only on the border, and floor in the center
    Mac Gyver is in area 2,8
    the villain is in area 13,13
    items are between them
    """
    with open('./maze.txt', 'w') as file:
        for _ in range(width):
            file.write('M ')
        file.write("\n")
        for _ in range(height - 2):
            file.write('M ')
            for _ in range(width - 2):
                file.write("S ")
            file.write('M\n')
        for _ in range(width):
            file.write('M ')

        file.write('\n\n')  # writing characters
        file.write('Mac Gyver\t1\t1\n')
        file.write('Keeper\t13\t13\tneedle\tpipe\tsyringe\t')

        file.write("\n\n")  # writing items
        file.write("needle\n")
        file.write("pipe\n")
        file.write("syringe\n")

if __name__ == "__main__":
    create_maze(15, 15)
