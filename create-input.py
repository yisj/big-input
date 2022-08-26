import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

line = ""

for _ in range(1000000):
	line += random.choice(chars)

with open('input.txt', 'w') as f:
	f.write(line)