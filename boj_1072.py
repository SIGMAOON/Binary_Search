# 게임
X,Y = map(int,input().split())
Z = int(100*Y/X)

start = 1
end = 10000000000

while start < end:
  mid = (start+end)//2
  newZ = int(100*(Y+mid)/(X+mid))

  if newZ <= Z:
    start = mid+1
  else:
    end = mid

if int(100*(Y+end)/(X+end)) > Z:
  print(end)
else:
  print(-1)