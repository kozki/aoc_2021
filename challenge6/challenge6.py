def magic(con, d):
    for day in range(d):
        new_counter = Counter()
        for i in list(con.keys()):
            if i == 0:
                new_counter[6] += con[i]
                new_counter[8] += con[i]
            else:
                new_counter[i-1] += con[i]
        con = new_counter
    return sum(con.values())


if __name__ == '__main__':
    from collections import Counter

    content = open('input.txt').readline().strip().split(',')
    content_list = content
    content = Counter(list(map(int, content)))

    # part1 and part2 --------------------------------------------------------------------------------------------------
    print('Part1 answer: ', magic(content, 80))
    print('Part2 answer: ', magic(content, 256))
