from itertools import chain
plist=[[2,4,3],[1,5,6],[9],[7,9,0]]
result = list(chain.from_iterable(plist))
print(result)