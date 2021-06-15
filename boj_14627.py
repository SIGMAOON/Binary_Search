# 파닭파닭. 수정 필요
pa_num,chicken = map(int,input().split())
pas = []
for _ in range(pa_num):
  pas.append(int(input()))

pa_total = sum(pas)

start = 1
end = pa_total//chicken
answer = []
while start<=end:
  mid = (start+end)//2
  count = 0
  for pa in pas:
    count+=int(pa/mid)
  if count > chicken:
    start = mid + 1
  elif count == chicken:
    answer.append(mid)
    start = mid+1
  else:
    end = mid - 1
print(pa_total - max(answer)*chicken)
