# K번째 수
# A는 N*N 행렬, A[i][j] = i*j
# B는 A의 오름차순, B[k] = ?
N = int(input())
k = int(input())

start = 1
end = k

while start<= end:
  mid = (start+end)//2
  cnt = 0
  for i in range(1,N+1):
    cnt+=min(N,mid//i)
  
  if cnt < k:
    start = mid + 1
  else:
    end = mid - 1
  
print(start)
