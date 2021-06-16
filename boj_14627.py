# 파닭파닭. 수정 필요
pa_num,chicken = map(int,input().split())
pas = [int(input()) for _ in range(pa_num)]

pa_total = sum(pas)

start = 1
end = pa_total//chicken

answer = []

while start<=end:
  mid = (start+end)//2
  cnt = 0
  for pa in pas:
    cnt+=int(pa/mid)
  if cnt == chicken:
    answer.append(mid)
  if cnt >= chicken:
    start = mid + 1
  else:
    end = mid - 1
print(pa_total - max(answer)*chicken)