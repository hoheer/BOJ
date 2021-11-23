lst = []
for i in range(0,9):
  num = int(input())
  lst.append(num)

print(max(lst))
m_index = lst.index(max(lst))
m_index+=1
print(m_index)
