import itertools
import os

def iterator_offset(iterable, offset):
    items, nexts = itertools.tee(itertools.cycle(iterable), 2)
    nexts = itertools.chain(itertools.islice(nexts, offset, None))
    return zip(items, nexts)

def sum_matches(captcha, offset):
    i = 0
    sum_pair = 0
    for item, nxt in iterator_offset(captcha, offset):
        if i == len(captcha):
            break
        else:
            i += 1
            if int(item) == int(nxt):
                sum_pair += int(item)

    print(sum_pair)
    return sum_pair

def read_captcha():
    with open(os.path.join("advent_of_code", "input", "day1_captcha.txt"), "r") as f:
        for line in f:
            captcha = line.rstrip()
    return captcha

input_captcha = read_captcha()
sum_matches(input_captcha, 1)
sum_matches(input_captcha, int(len(input_captcha)/2))
