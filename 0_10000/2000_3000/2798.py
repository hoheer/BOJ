import itertools as iter
n,m = map(int,input().split())
card =list(map(int,input().split()))

max = 0
answer=[]
for cards in iter.combinations(card,3):
  tsum = sum(cards)
  if(tsum>max and m>=tsum):
    max = tsum
    answer = cards

print(max)
