import time


if __name__ == '__main__':
    start_time = time.time()
    content = open('../input.txt').readline().strip().split(',')
    content = list(map(int, content))
    max = max(content)

    # part1
    # scores = {}
    # counter = 1
    # for i in range(max):
    #     distance = 0
    #     for j in content:
    #         if i <= j:
    #             distance += j - i
    #         else:
    #             distance += i - j
    #         counter += 1
    #     scores[i] = distance
    #
    # print(content)
    # print(scores)
    # min_key = min(scores, key=scores.get)
    # print(scores[min_key])

    # part2
    # scores = {}
    # for i in range(max):
    #     distance = 0
    #     for j in content:
    #         if i <= j:
    #             distance += sum(range(1, (j - i) + 1))
    #         else:
    #             distance += sum(range(1, (i - j) + 1))
    #     print('ITERACIJA:', i, distance)
    #     scores[i] = distance
    #
    # print(content)
    # print(scores)
    # min_key = min(scores, key=scores.get)
    # print(scores[min_key])

    # part2 optimized
    scores = {}
    for i in range(max):
        scores[i] = sum((map(lambda x: sum(range(1, abs(x - i) + 1)), content)))
        print('ITERACIJA:', i, scores[i])

    min_key = min(scores, key=scores.get)
    print(scores[min_key])
    print("--- %s seconds ---" % (time.time() - start_time))

