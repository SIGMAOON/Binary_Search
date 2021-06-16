# 어두운 굴다리
def cover_check(bridge,cover):
  # 맨 앞, 맨 뒤 처리 후 가운데 처리
  if (bridge[1] - bridge[0]) > cover:
    return False
  if (bridge[-1]- bridge[-2]) > cover:
    return False
  for i in range(1,len(bridge)-2):
    if (bridge[i+1] - bridge[i])/2 > cover:
      return False
  return True
  
N = int(input()) # 굴다리의 길이
M = int(input()) # 가로등의 개수
x = list(map(int,input().split())) # 가로등의 위치

bridge = [0] + x + [N]

start,end = 0,N
height = 0

while start<=end:
  mid = (start+end)//2
  if cover_check(bridge,mid):
    end = mid - 1
    height = mid
  else:
    start = mid + 1

print(height)