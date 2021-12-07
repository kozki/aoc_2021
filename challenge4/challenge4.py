def remove_element(n, list):
    return [['-1' if str(i) == str(n) else i for i in sub] for sub in list]


def all_same(items, x):
    return all(x == items[0] for x in items)


def winning_board(list):
    for l in range(len(list)):
        if all_same(list[l], '-1'):
            return True
        elif list[0][l] == list[1][l] == list[2][l] == list[3][l] == list[4][l] == '-1':
            return True
    return False


def get_score(list):
    l = [[int(float(j)) for j in i if j != '-1'] for i in list]
    return sum([sum(x) for x in l])


def get_loosing_board(boards):
    from operator import itemgetter
    return max(boards.items(), key=itemgetter(1))[1][1]


if __name__ == '__main__':
    content = [x for x in open('input.txt').read().strip().split('\n')]

    # part1 ------------------------------------------------------------------------------------------------------------
    numbers = str(content[0]).split(",")
    boards = {}
    content = [x for x in content[1:] if x]
    composite_list = [content[x:x+5] for x in range(0, len(content), 5)]

    counter = 0
    for l in composite_list:
        new_list = []
        for i in l:
            new_list.append(str(i).split())
        boards[counter] = new_list
        counter += 1

    winning = []
    winning_boards = {}
    win_order = 1
    for n in numbers:
        for key, value in boards.items():
            boards[key] = remove_element(n, value)
            if winning_board(boards[key]):
                score = get_score(boards[key])
                res = int(n) * int(score)
                winning.append(res)
                if key not in winning_boards.keys():
                    winning_boards[key] = (win_order, res)
                    win_order += 1

    print('Part1 answer: ', winning[0])

    # part2 ------------------------------------------------------------------------------------------------------------
    print('Part2 answer: ', get_loosing_board(winning_boards))
