if __name__ == '__main__':
    content = open('input.txt').readline().strip().split(',')
    content = list(map(int, content))
    max_item = max(content)

    # part1 ------------------------------------------------------------------------------------------------------------
    scores = {}
    counter = 1
    for i in range(max_item):
        distance = 0
        for j in content:
            if i <= j:
                distance += j - i
            else:
                distance += i - j
            counter += 1
        scores[i] = distance

    min_key = min(scores, key=scores.get)
    print('Part1 answer: ', scores[min_key])

    # part2 ------------------------------------------------------------------------------------------------------------
    scores = {}
    for i in range(max_item):
        distance = 0
        for j in content:
            if i <= j:
                distance += sum(range(1, (j - i) + 1))
            else:
                distance += sum(range(1, (i - j) + 1))
        scores[i] = distance

    min_key = min(scores, key=scores.get)
    print('Part2 answer: ', scores[min_key])

    # part2 minimized --------------------------------------------------------------------------------------------------
    scores = {}
    for i in range(max_item):
        scores[i] = sum((map(lambda x: sum(range(1, abs(x - i) + 1)), content)))

    min_key = min(scores, key=scores.get)
    print('Part2 minimized answer: ', scores[min_key])

