""" génération d'une map pour faire des tests. """


def createMaze(width,height):
    with open('maze.txt', 'w') as f:
        for i in range(width):
            f.write('M ')
        f.write("\n")
        for i in range(height-2):
            f.write("M ")
            for j in range(width-2):
                f.write("S ")
            f.write('M\n')
        for i in range(width):
            f.write('M ')
        f.write('\n\n')
        f.write('Mac Gyver\t2\t7\n')
        f.write('Garde\t18\t8')
        # TODO f.write pour chaque objet.

if __name__=="__main__":
    createMaze(20,10)