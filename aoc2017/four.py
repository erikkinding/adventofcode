# -*- coding: utf-8 -*-


def part_one():
    file = open('input/four.txt', 'r')
    rows = file.read().splitlines()

    valid_passwords = 0
    for password in rows:

        segments_count = {}
        segments = password.split()
        valid = True
        for s in segments:
            if segments_count.get(s) is not None:
                # invalid pass phrase
                valid = False
                break
            else:
                segments_count[s] = 1
        if valid:
            valid_passwords += 1

    print("valid passwords: ", valid_passwords)


def part_two():
    file = open('input/four.txt', 'r')
    rows = file.read().splitlines()

    valid_passwords = 0
    for password in rows:

        segments_count = {}
        segments = password.split()
        valid = True
        for s in segments:
            sorted_s = ''.join(sorted(s))
            if segments_count.get(sorted_s) is not None:
                # invalid pass phrase
                valid = False
                break
            else:
                segments_count[sorted_s] = 1
        if valid:
            valid_passwords += 1

    print("valid passwords with anagram check: ", valid_passwords)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
