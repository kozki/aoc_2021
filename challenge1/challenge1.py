if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        content = [int(line.rstrip()) for line in lines]

        # part1 --------------------------------------------------------------------------------------------------------
        counter = 0
        for i in range(len(content)-1):
            prev = int(content[i])
            next = int(content[i+1])
            if next > prev:
                counter = counter + 1
        print('Part1 answer: ', counter)

        # part2 --------------------------------------------------------------------------------------------------------
        counter = 0

        for i in range(0, len(content) - 3):
            sum1 = sum(content[i:i + 3])
            sum2 = sum(content[i + 1:i + 4])
            if sum1 < sum2:
                counter = counter + 1
        print('Part2 answer: ', counter)


