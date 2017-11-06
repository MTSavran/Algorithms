from collections import defaultdict
edges = {1:[(8,3),(7,4)], 7:[(11,6)], 8:[(11,9)]}
reverse = defaultdict(list)
for i in edges:
        for x in edges[i]:
            reverse[x[0]].append((i,x[1]))

#print reverse


SS = set()
ST=set()

SS.add(5)
ST.add(7)
ST.add(5)

SNew = SS.union(ST)

print SNew