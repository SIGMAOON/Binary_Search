# 공유기 설치
def count_wifi(lists,mid):
  cnt = 1
  before = lists[0]
  for i in range(1,len(lists)):
    if lists[i] >= before + mid:
      cnt+=1
      before = lists[i]
  return cnt

h,wifi = map(int,input().split())
home = sorted([int(input()) for _ in range(h)])

start = 1
end = home[-1] - home[0]
answer =0

while start<=end:
  mid = (start+end)//2

  x = count_wifi(home,mid)

  if x >= wifi:
    start = mid + 1
  else:
    end = mid - 1

print(answer)