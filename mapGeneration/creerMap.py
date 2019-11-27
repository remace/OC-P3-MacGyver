""" map generation for tests """


def create_maze(width, height):
    with open('../maze.txt', 'w') as f:
        for i in range(width):
            f.write('M ')
        f.write("\n")
        for i in range(height - 2):
            f.write('M ')
            for j in range(width - 2):
                f.write("S ")
            f.write('M\n')
        for i in range(width):
            f.write('M ')

        f.write('\n\n')  # writing characters
        f.write('Mac Gyver\t2\t8\n')
        f.write('Keeper\t6\t8\tneedle\tpipe\tsyringe\t')

        f.write("\n\n")  # writing items
        f.write("needle\t3\t8\n")
        f.write("pipe\t4\t8\n")
        f.write("syringe\t5\t8\n")


if __name__ == "__main__":
    create_maze(10, 10)
