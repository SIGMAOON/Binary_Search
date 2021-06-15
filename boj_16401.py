# 과자 나눠주기
joca,snackN = map(int,input().split())
snack = list(map(int,input().split())) # 정렬되어있음

start,end = 1, max(snack)
length = 0
while start<=end:
  mid = (start+end)//2
  cnt = 0
  for yamyam in snack:
    cnt+= yamyam//mid
  
  if cnt >= joca:
    length = mid
    start = mid + 1
  else:
    end = mid - 1

print(length)