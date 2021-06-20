# 입국 심사
import sys
gate,sangs = map(int,sys.stdin.readline().split())
gates = [int(sys.stdin.readline()) for _ in range(gate)]

start = min(gates)
end = max(gates)*sangs
answer = 0

while start<=end:
  mid = (start+end)//2
  total = 0
  for g in gates:
    total += mid//g
  if total < sangs:
    start = mid + 1
  else:
    end = mid - 1
    answer = mid

print(answer)