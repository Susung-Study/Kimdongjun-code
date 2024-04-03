n = int(input())
result = 0
time = list(map(int, input().split()))
time.sort()

for i in range(len(time)):
  result += sum(time[0:i+1])

print(result)

