# 용돈 관리
def Mcountdown(lists,k):
  total = 0
  cnt = 1
  for money in lists:
    if total+money > k:
      cnt+=1 # 인출 범위를 넘어가면 한 번 더 인출해야함
      total = money # 새로 인출함. 초기화.
    else:
      total+=money

  return cnt

N,M = map(int,input().split())
use = []
for _ in range(N):
  use.append(int(input()))

start = max(use) # 매일 인출이 가능하려면,,,,
end = sum(use) # 한 번만 인출하면 됨

while start<=end:
  mid = (start+end)//2
  if Mcountdown(use,mid) <= M:
    end = mid - 1
  else:
    start = mid + 1

print(mid)