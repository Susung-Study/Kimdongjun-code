n,k = map(int,input().split())
coin = []
answer = 0
for i in range(n):
  coin.append(int(input()))
  
coin.reverse()

for c in coin:
  answer += (k//c)
  k = k%c

print(answer)