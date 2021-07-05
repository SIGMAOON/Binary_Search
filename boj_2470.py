# 두 용액
import sys
N = int(input())
portion = sorted(list(map(int,sys.stdin.readline().split())))

start = 0
end = len(portion) - 1
minimum = sys.maxsize
pair = []
while start<end:
  answer = portion[start]+portion[end]
  
  if abs(answer) < minimum:
    pair = [portion[start],portion[end]]
    minimum = abs(answer)

  if answer < 0:
    start +=1
  else:
    end-=1

print(pair[0],pair[1])