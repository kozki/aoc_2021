from collections import Counter


def contains(s1, s2):
    s2set = Counter(s2)
    return all(count <= s2set[c] for c, count in Counter(s1).items())


if __name__ == '__main__':
    from Levenshtein import distance as levenshtein_distance, distance

    # content = [str(x).strip().split(" | ") for x in open('input_little.txt').read().strip().split('\n')]
    content = [str(x).strip().split(" | ") for x in open('input_little.txt').readline().strip().split('\n')]
    numbers = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

    print(content)

    # part2 ------------------------------------------------------------------------------------------------------------
    # for r in range(1, len(content)):
    res = {}
    other = []
    for c in content:
        for i in c[0].split(" "):
            if len(i) == 2:
                res[i] = 1
            if len(i) == 3:
                res[i] = 7
            if len(i) == 4:
                res[i] = 4
            if len(i) == 7:
                res[i] = 8
            if len(i) == 5:
                other.append(i)
                res[i] = [2, 3, 5]
            if len(i) == 6:
                other.append(i)
                res[i] = [0, 6, 9]

    print(other)
    print(res)

    for i in other:
        for j in other:
            # print(i, j, distance(i, j))
            if distance(i, j) == 2:
                if len(i) == 5:
                    res[i] = 5
                    res[j] = 6
                else:
                    res[j] = 5
                    res[i] = 6
            if distance(i, j) == 3:
                if len(i) == 6 and len(j) == 5 and res[j] == 5:
                    res[i] = 9
                if len(i) == 5 and len(j) == 6 and res[i] == 5:
                    res[j] = 9
                if len(i) == 6 and len(j) == 6 and res[i] == 6:
                    res[j] = 0
                if len(i) == 6 and len(j) == 6 and res[j] == 6:
                    res[i] = 0
                if len(i) == 5 and len(j) == 5 and res[i] == 5:
                    res[j] = 2
                if len(i) == 5 and len(j) == 5 and res[j] == 5:
                    res[i] = 2
            if distance(i, j) == 4:
                if len(i) == 6 and len(j) == 5 and res[i] == 9:
                    res[j] = 3
                if len(i) == 5 and len(j) == 6 and res[j] == 9:
                    res[i] = 3
    # print(res)
    #
    # print(content[0][1].split(" "))

    final_res = ""
    for c in content[0][1].split(" "):
        if len(c) == 2:
            bla = {k: v for k, v in res.items() if v == 1}
            final_res += str(bla)
        elif len(c) == 3:
            bla = {k: v for k, v in res.items() if v == 7}
            final_res += str(bla)
        elif len(c) == 4:
            bla = {k: v for k, v in res.items() if v == 4}
            final_res += str(bla)
        elif len(c) == 7:
            bla = {k: v for k, v in res.items() if v == 8}
            final_res += str(bla)
        else:
            for j in res.keys():
                if contains(c, j) and len(c) == len(j):
                    final_res += str(res[j])

    print(final_res)




    # print('Part1 answer: ', counter)
    # print('Part1 answer: ', res)









