# IF문 좀 대신 써줘
import sys
N, M = map(int, sys.stdin.readline().split())
NamePower = [sys.stdin.readline().split() for _ in range(N)]
for _ in range(M):
  start = 0
  end = len(NamePower) - 1
  x =  int(sys.stdin.readline())

  while start<=end:
    mid = (start+end)//2
    if x <= NamePower[mid][1]:
      end = mid - 1
    else:
      start = mid + 1

  print(NamePower[start][0]) 