# 장난감 경주 . 수정필요
# 트랙의 길이 X
# 1~N번까지의 번호, 나는 N번
# i번 참가자의 속도는 V[i]
# 나는 부스터가 있지, 처음 1초간 Zm/s로 달림 나머진 V[N]
# 그러면 이 때 걸리는 시간은 1+(X-Z)/V[N]
# Z값은 부스터 최대값 Y 이하
# 내가 단독우승하기위한 최소의 Z값
# 부스터 없어도 되면 0, 최대로도 우승못하면 -1
# 입력 T(케이스 수)/N,X,Y 와 V 두 줄이 한 케이스 

T = int(input())

for _ in range(T):
  N,X,Y = map(int,input().split())
  V = list(map(int,input().split()))
  fastest = X/max(V[:-1]) # 나를 제외하고 가장 최단시간에 들어온 사람의 시간
  if X/V[-1] < fastest:
    print(0)
  elif 1+((X-Y)/V[-1]) >= fastest:
    print(-1)
  else:
    start = 0
    end = Y
    while start < end:
      mid = (start+end)//2
      if 1+((X-mid)/V[-1]) < fastest:
        end = mid - 1
      else:
        start = mid + 1
    print(mid)
