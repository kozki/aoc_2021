if __name__ == '__main__':
    with open('input.txt') as f:
        content = [list(x) for x in f.read().splitlines()]

    opening = "([{<"
    closing = ")]}>"
    points_1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
    points_2 = {")": 1, "]": 2, "}": 3, ">": 4}

    # part1 ------------------------------------------------------------------------------------------------------------
    res = 0
    scores = []
    for c in content:
        expected = []
        res2 = 0
        for i in range(len(c)):
            if c[i] in opening:
                expected.append(closing[opening.index(c[i])])
            elif expected[-1] != c[i]:
                res += points_1.get(c[i])
                break
            else:
                expected = expected[:-1]
        else:
            for i in reversed(expected):
                res2 = res2 * 5 + points_2.get(i)
            scores.append(res2)
    scores.sort()
    print('Part1 answer: ', res)
    print('Part2 answer: ', scores[int(len(scores)/2)])
