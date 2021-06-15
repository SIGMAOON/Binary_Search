# 기타 레슨
def blue_ray(lists,mid):
  cnt = 1
  total = 0
  for l in lists:
    if total+l > mid:
      cnt+=1
      total = l
    else:
      total+=l
  return cnt

N,M = map(int,input().split())
lesson = list(map(int,input().split()))

start = max(lesson)
end = sum(lesson)

while start<=end:
  mid = (start+end)//2
  if blue_ray(lesson,mid) <= M:
    end = mid - 1
  else:
    start = mid + 1 

print(start)