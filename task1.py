#task1.py
import sys

def rotate(A,B,C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

def grahamscan(A):
  n = len(A)
  P = range(n)
  for i in range(1,n):
    if A[P[i]][0]<A[P[0]][0]:
      P[i], P[0] = P[0], P[i]
  for i in range(2,n):
    j = i
    while j>1 and (rotate(A[P[0]], A[P[j-1]], A[P[j]]) < 0): 
      P[j], P[j-1] = P[j-1], P[j]
      j -= 1
  S = [P[0],P[1]]
  for i in range(2,n):
    while rotate(A[S[-2]], A[S[-1]], A[P[i]]) < 0:
      del S[-1]
    S.append(P[i])
  return S

points = []
for point in open(sys.argv[1]):
  points.append([int(i) for i in point.split()])

out = open(sys.argv[2], 'w')
for point in grahamscan(points):
	out.write(str(point+1)+'\n')
