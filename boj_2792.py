# 보석 상자.pypy3
def count_people(lists,mid):
  cnt = 0
  for num in lists:
    a = num//mid
    b = num%mid
    cnt += a
    if b != 0:
      cnt +=1
  return cnt

child,color = map(int,input().split())
jewl = sorted([int(input()) for _ in range(color)])

start = 1
end = jewl[-1]

while start < end:
  mid = (start+end)//2
  if count_people(jewl,mid) <= child:
    end = mid
  else:
    start = mid + 1


print(end)