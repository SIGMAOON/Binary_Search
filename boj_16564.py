# 히오스 프로게이머
def total(lists,K):
  total = 0
  for xi in lists:
    if xi >= K:
      return total
    total += (K-xi) 
  return total
    
N,K = map(int,input().split())
X = sorted([int(input()) for _ in range(N)])

start,end = min(X),max(X) + K
answer = 0
while start<=end:
  mid = (start+end)//2
  if total(X,mid) <= K: # total이 K보다 작아야함
    answer = mid
    start = mid + 1
  else:
    end = mid - 1

print(answer)