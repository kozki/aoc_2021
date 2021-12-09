if __name__ == '__main__':
    with open('input_little.txt') as f:
        content = [list(x) for x in f.read().splitlines()]
    # part1 ------------------------------------------------------------------------------------------------------------
    lowest = []

    for i in range(len(content)):
        neighbours = []
        for j in range(len(content[i])):
            if i == 0:
                # upper left corner
                if j == 0:
                    neighbours = [content[i][j + 1], content[i + 1][j + 1], content[i + 1][j]]
                # upper edge
                elif j != len(content[i]) - 1:
                    neighbours = [content[i][j - 1], content[i + 1][j], content[i][j + 1]]
                # upper right corner
                else:
                    neighbours = [content[i + 1][j], content[i + 1][j - 1], content[i][j - 1]]
            elif j == len(content[i]) - 1:
                # right edge
                if i != len(content) - 1:
                    neighbours = [content[i - 1][j], content[i][j - 1], content[i + 1][j]]
                # lower right corner
                else:
                    neighbours = [content[i][j - 1], content[i - 1][j - 1], content[i - 1][j]]
            elif i == len(content) - 1:
                # lower left corner
                if j == 0:
                    neighbours = [content[i - 1][j], content[i - 1][j + 1], content[i][j + 1]]
                # lower edge
                elif j != len(content[i]) - 1:
                    neighbours = [content[i][j + 1], content[i][j - 1], content[i - 1][j]]
            elif j == 0 and i != 0:
                # left edge
                if i != len(content):
                    neighbours = [content[i - 1][j], content[i][j + 1], content[i + 1][j]]
            else:
                neighbours = [content[i - 1][j], content[i][j + 1], content[i + 1][j], content[i][j - 1]]
            neighbours = [int(x) for x in neighbours]
            if min(neighbours) > int(content[i][j]):
                lowest.append(int(content[i][j]) + 1)

    print('Part1 answer: ', sum(lowest))


