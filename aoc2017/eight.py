# -*- coding: utf-8 -*-

import aoc

inp = aoc.input_as_rows("eight.txt")

max_value = {"m": 0}
registers = {}

def check_condition(expr):
	seg = expr.split()

	a = get_value(seg[0])
	op = seg[1]
	b = seg[2]

	if op == ">":
		return int(a) > int(b)
	elif op == "<":
		return int(a) < int(b)
	elif op == ">=":
		return int(a) >= int(b)
	elif op == "<=":
		return int(a) <= int(b)
	elif op == "==":
		return int(a) == int(b)
	elif op == "!=":
		return int(a) != int(b)

	print("this is wrong...")
	return False

def get_value(key):
	if key in registers:
		return registers[key]
	else:
		registers[key] = 0
		return 0

def update_max(new_value):
	if new_value > max_value["m"]:
		max_value["m"] = new_value

def update_register(key, value, op):
	if op == "dec":
		value *= -1
	new_value = get_value(key) + value
	update_max(new_value)
	registers[key] = new_value
	

def part1():

	for instruction in inp:
		segments = instruction.split("if")
		condition = segments[1]

		if check_condition(condition):
			inst = segments[0].split()
			register = inst[0]
			op = inst[1]
			value = int(inst[2])
			update_register(register, value, op)
			
	print("Register with biggest value: ", sorted(registers.items(), key = lambda x: x[1])[-1:])
	

def part2():
	print("Max value during execution: ", max_value.items())

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()