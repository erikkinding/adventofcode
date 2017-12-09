# -*- coding: utf-8 -*-

import aoc
inp = aoc.input_as_string("nine.txt")


def replace_negations(text):

    # Remove all ! and following negated char
    while True:
        try:
            index = text.index('!')
            text = text[:index] + text[index+2:]
        except:
            break

    return text


def clean_input(text):

    # simplify negations
    text = replace_negations(text)

    # clean garbage
    cleaned = ""
    garbage = False
    garbage_count = 0

    for c in text:

        # enter garbage section
        if c == '<' and not garbage:
            garbage = True
            continue

        # exit garbage section
        if c == '>' and garbage:
            garbage = False
            continue

        if not garbage:
            cleaned += c
        else:
            garbage_count += 1

    print("GC count: ", garbage_count)

    return cleaned


def count_groups(text):

    level = 0
    score = 0
    for c in text:
        if c == "{":
            level += 1

        if c == "}":
            score += level
            level -= 1

    return score


# answer 12803
def part1():
    print("Part 1: ", count_groups(clean_input(inp)))


def part2():
    print("part2: see GC count from part 1")


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()