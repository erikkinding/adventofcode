# -*- coding: utf-8 -*-

inp = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]
#inp = [0, 2, 7, 0]
inp_len = len(inp)
memory = inp

def redistribute_memory(index):
    value = memory[index]
    memory[index] = 0

    while value > 0:
        index += 1
        memory[index % inp_len] += 1
        value -= 1


def mem_hash():
    return '_'.join(map(str, memory))


def part_one():
    
    state_cache = {}
    state_cache[mem_hash()] = 1

    reallocations = 0
    while True:
        mem_max_index = memory.index(max(memory))
        redistribute_memory(mem_max_index)
        reallocations += 1

        new_mem_hash = mem_hash()
        if new_mem_hash in state_cache:
            break
        else:
            state_cache[new_mem_hash] = 1

    return reallocations


def part_two():
    # reset state if part_one was run before:
    inp_len = len(inp)
    memory = inp
    
    part_one()
    return part_one()


def main():
    print("Reallocations: ", part_one())
    print("Loop size: ", part_two())


if __name__ == "__main__":
    main()
