# 접두사 찾기,pypy3 -> python3 방법 찾기
N,M = map(int,input().split())
string = [input() for _ in range(N)]
cnt = 0
for _ in range(M):
  prefix = input()
  for s in string:
    if prefix == s[:len(prefix)]:
      cnt+=1
      break
print(cnt)