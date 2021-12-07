from itertools import chain
from collections import Counter


def print_board(board):
    for b in board:
        print(b)


def calculate_sum(board):
    return Counter(chain(*[x for x in board]))


def part1(board, new_content):
    for i in new_content:
        if int(i[1]) == int(i[3]):
            if int(i[0]) < int(i[2]):
                for j in range(int(i[0]), int(i[2]) + 1):
                    board[int(i[3])][j] += 1
            elif int(i[2]) < int(i[0]):
                for j in range(int(i[2]), int(i[0]) + 1):
                    board[int(i[3])][j] += 1
        elif int(i[0]) == int(i[2]):
            if int(i[1]) < int(i[3]):
                for j in range(int(i[1]), int(i[3]) + 1):
                    board[j][int(i[2])] += 1
            elif int(i[3]) < int(i[1]):
                for j in range(int(i[3]), int(i[1]) + 1):
                    board[j][int(i[2])] += 1
    return board


def part2(board, new_content):
    for i in new_content:
        if int(i[1]) == int(i[3]):
            if int(i[0]) < int(i[2]):
                for j in range(int(i[0]), int(i[2]) + 1):
                    board[int(i[3])][j] += 1
            elif int(i[2]) < int(i[0]):
                for j in range(int(i[2]), int(i[0]) + 1):
                    board[int(i[3])][j] += 1
        elif int(i[0]) == int(i[2]):
            if int(i[1]) < int(i[3]):
                for j in range(int(i[1]), int(i[3]) + 1):
                    board[j][int(i[2])] += 1
            elif int(i[3]) < int(i[1]):
                for j in range(int(i[3]), int(i[1]) + 1):
                    board[j][int(i[2])] += 1
        else:
            counter_x1 = int(i[0])
            counter_y1 = int(i[1])
            counter_x2 = int(i[2])
            counter_y2 = int(i[3])
            for j in range(0, abs(int(i[0]) - int(i[2])) + 1):
                board[counter_x1][counter_y1] += 1
                if counter_x1 >= counter_x2 and counter_y1 >= counter_y2:
                    counter_x1 -= 1
                    counter_y1 -= 1
                elif counter_x1 <= counter_x2 and counter_y1 <= counter_y2:
                    counter_x1 += 1
                    counter_y1 += 1
                elif counter_x1 <= counter_x2 and counter_y1 >= counter_y2:
                    counter_x1 += 1
                    counter_y1 -= 1
                elif counter_x1 >= counter_x2 and counter_y1 <= counter_y2:
                    counter_x1 -= 1
                    counter_y1 += 1
    return board


if __name__ == '__main__':
    content = [str(x).split(" -> ") for x in open('input.txt').read().strip().split('\n')]

    # part1 ------------------------------------------------------------------------------------------------------------
    new_content = []
    for c in content:
        new_content.append(str(c[0]).split(',') + str(c[1]).split(','))

    max_item = int(max([sublist[-1] for sublist in new_content])) + 1
    board = [[0 for x in range(int(max_item))] for x in range(int(max_item))]

    p1 = part1(board, new_content)
    # print_board(p1)
    res1 = calculate_sum(p1)
    res1 = sum(v for k, v in res1.items() if k >= 2)
    print('Part1 answer: ', res1)

    # part2 ------------------------------------------------------------------------------------------------------------
    board = [[0 for x in range(int(max_item))] for x in range(int(max_item))]
    p2 = part2(board, new_content)
    # print_board(p2)
    res2 = calculate_sum(p2)
    res2 = sum(v for k, v in res2.items() if k >= 2)
    print('Part2 answer: ', res2)





