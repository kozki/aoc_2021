if __name__ == '__main__':
    with open('input.txt') as f:
        content = f.read().splitlines()

        # part1 --------------------------------------------------------------------------------------------------------
        ones = [0] * len(content[0])
        zeros = [0] * len(content[0])

        for i in content:
            for j in range(len(i)):
                if int(i[j]) == 0:
                    zeros[j] += 1
                else:
                    ones[j] += 1

        gamma = ""
        epsilon = ""
        for i in range(len(ones)):
            if ones[i] > zeros[i]:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"

        gamma_d = int(gamma, 2)
        epsilon_d = int(epsilon, 2)
        print('Part1 answer: ', gamma_d * epsilon_d)

        # part2 --------------------------------------------------------------------------------------------------------
        from collections import Counter
        new_content = content

        theta = ''
        epsilon = ''
        for i in range(len(new_content[0])):
            common = Counter([x[i] for x in new_content])

            if common['0'] > common['1']:
                new_content = [x for x in new_content if x[i] == '0']
            else:
                new_content = [x for x in new_content if x[i] == '1']
            theta = new_content[0]

        for i in range(len(content[0])):
            common = Counter([x[i] for x in content])

            if common['0'] > common['1']:
                content = [x for x in content if x[i] == '1']
            else:
                content = [x for x in content if x[i] == '0']
            if content:
                epsilon = content[0]
        print('Part2 answer: ', int(theta, 2) * int(epsilon, 2))

