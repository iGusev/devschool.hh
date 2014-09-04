#task2.py
import sys

seq_lines = [int(line) for line in open(sys.argv[1])]
out = open(sys.argv[2], 'w')

for seq in seq_lines:
  line = [i for i in range(int(str(seq)[0]), seq)]
  s = ''.join([str(x) for x in line])
  pos = s.find(str(seq)) + 1
  out.write(str(pos)+'\n')
