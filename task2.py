seq_lines = [line.strip() for line in open('task2')]
line = [i for i in range(1,10000000)]

for seq in seq_lines:
	s = ''.join([str(x) for x in line])
	pos = s.find(str(seq)) + 1
	print pos
