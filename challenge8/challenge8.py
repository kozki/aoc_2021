if __name__ == '__main__':
    content = [str(x).strip().split(" | ")[1].split(" ") for x in open('input.txt').read().strip().split('\n')]
    numbers = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

    # part1 ------------------------------------------------------------------------------------------------------------
    counter = 0
    for c in content:
        for i in c:
            if len(i) in [2, 3, 4, 7]:
                counter += 1
    print('Part1 answer: ', counter)







