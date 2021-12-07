if __name__ == '__main__':
    with open('input.txt') as f:
        content = f.read().splitlines()

        depth = 0
        horizontal = 0

        # part1 --------------------------------------------------------------------------------------------------------
        for i in content:
            text = str(i).split(" ")
            command = text[0]
            count = text[1]

            if command == "forward":
                horizontal += int(count)
            elif command == "down":
                depth += int(count)
            elif command == "up":
                depth -= int(count)
        print('Part1 answer: ', depth * horizontal)

        # part2 --------------------------------------------------------------------------------------------------------
        depth = 0
        horizontal = 0
        aim = 0
        for i in content:
            text = str(i).split(" ")
            command = text[0]
            count = text[1]

            if command == "forward":
                horizontal += int(count)
                depth += (int(aim) * int(count))
            elif command == "down":
                aim += int(count)
            elif command == "up":
                aim -= int(count)
        print('Part2 answer: ', depth * horizontal)

