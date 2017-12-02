# -*- coding: utf-8 -*-

def partOne():
	file = open('input/two.txt', 'r')
	rows = file.read().splitlines()

	checksum = 0
	for r in rows:
		values = r.split()

		rowMax = 0
		rowMin = 10000000000
		for v in values:
			if int(v) > rowMax: 
				rowMax = int(v)
			if int(v) < rowMin:
				rowMin = int(v)

		checksum += (rowMax - rowMin);

	print("part 1: ", checksum)
	
# 111 too low
def partTwo():
	file = open('input/two.txt', 'r')
	rows = file.read().splitlines()

	checksum = 0
	for r in rows:
		i = 0
		values = r.split()
		while(i < len(values)):
			k = 0
			a = int(values[i])
			while(k < len(values)):
				b = int(values[k])
				if(i != k and a % b == 0):
					checksum += (a / b);
				k += 1

			i += 1

	print("part 2: ", checksum)
	
def main():
	partOne()
	partTwo()

if __name__ == "__main__":
	main()

