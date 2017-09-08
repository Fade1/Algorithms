import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--Elements", type=int, help="amount of elements")
args = parser.parse_args()
n = args.Elements

blocks = []
amount_of_blocks = (n * (n - 1)) / 6
existing_pairs = []


def random_suitable_element():
    flag1 = 'true'
    while flag1 == 'true':
        x = random.randint(1, n)
        x_counter = 0
        for block in blocks:
            if x in block:
                x_counter += 1
        if x_counter < (n - 1) / 2:
            flag1 = 'false'
    return x


def random_suitable_pair(x, second_digit):
    flag2 = 'true'
    while flag2 == 'true':
        flag3 = 'true'
        while flag3 == 'true':
            y = random.randint(1, n)
            if y != x and y != second_digit:
                flag3 = 'false'
        x_y_counter = 0
        for block in blocks:
            if x in block and y in block:
                x_y_counter += 1
        if x_y_counter == 0:
            flag2 = 'false'
    return y

while amount_of_blocks > 0:
    x = random_suitable_element()
    y = random_suitable_pair(x, 0)
    z = random_suitable_pair(x, y)
    pair_3 = [y, z, x]
    blocks_to_be_removed = []
    for block in blocks:
        if len(set(block).difference(set([y, z]))) == 1:
            blocks_to_be_removed.append(block)
            amount_of_blocks += 1

    for block in blocks_to_be_removed:
        blocks.remove(block)

    pair_3.sort()
    blocks.append(tuple(pair_3))
    amount_of_blocks -= 1

blocks.sort()
print(blocks)
print(len(blocks))

