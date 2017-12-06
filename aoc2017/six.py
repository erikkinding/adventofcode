# -*- coding: utf-8 -*-

inp = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]
#inp = [0, 2, 7, 0]
inp_len = len(inp)

def first_index_of(value, memory):
    for idx, mem_value in enumerate(memory):
        if mem_value == value:
            return idx


def redistribute_memory(index, memory):
    value = memory[index]
    memory[index] = 0

    while value > 0:
        index += 1
        memory[index % inp_len] += 1
        value -= 1

    return memory


def mem_hash(memory):
    return '_'.join(map(str, memory))


def part_one():
    memory = inp
    state_cache = {}
    state_cache[mem_hash(memory)] = 1

    reallocations = 0
    while True:
        mem_max_index = first_index_of(max(memory), memory)
        memory = redistribute_memory(mem_max_index, memory)
        reallocations += 1

        new_mem_hash = mem_hash(memory)
        if new_mem_hash in state_cache:
            break
        else:
            state_cache[new_mem_hash] = 1

    print("Part1 reallocations: ", reallocations)
    return memory


def part_two(memory):
    state_cache = {}
    state_cache[mem_hash(memory)] = 1

    reallocations = 0
    while True:
        mem_max_index = first_index_of(max(memory), memory)
        memory = redistribute_memory(mem_max_index, memory)
        reallocations += 1

        new_mem_hash = mem_hash(memory)
        if new_mem_hash in state_cache:
            break
        else:
            state_cache[new_mem_hash] = 1

    print("Part2 loop size: ", reallocations)


def main():
    looping_state = part_one()
    part_two(looping_state)


if __name__ == "__main__":
    main()
