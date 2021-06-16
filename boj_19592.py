# 장난감 경주 . 수정필요
T = int(input())

for _ in range(T):
  N,X,Y = map(int,input().split())
  V = list(map(int,input().split()))
  fastest = X/max(V[:-1]) # 나를 제외하고 가장 최단시간에 들어온 사람의 시간

  if fastest > X/V[-1]:
    print(0)
  elif 1+((X-Y)/V[-1]) >= fastest:
    print(-1)
  else:
    start = 0
    end = Y
    while start < end:
      mid = (start+end)//2
      if 1+((X-mid)/V[-1]) < fastest:
        end = mid
      else:
        start = mid + 1
    print(end)