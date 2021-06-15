# 먹을 것인가 먹힐 것인가
def findInx(lists,n):
  start = 0
  end = len(lists)-1
  idx = -1 # A[0]<=B[0]면 0 돌려줌 

  while start<=end:
    mid = (start+end)//2
    if lists[mid] < n:
      idx = mid
      start = mid + 1
    else:
      end = mid - 1
  return idx + 1 # 개수는 인덱스보다 하나 크니까,,,,
 
T = int(input())

for _ in range(T):
  cnt = 0
  numA,numB = map(int,input().split())
  A = sorted(list(map(int,input().split())))
  B = sorted(list(map(int,input().split())))

  for a in A:
    cnt+=findInx(B,a)

  print(cnt)  