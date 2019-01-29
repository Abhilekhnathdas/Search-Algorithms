print("Enter the edges if no edges need to be included write 'done'")
graphmatrix=[]
numtoval=dict({})
valtonum=dict({})
node=0
edges=[]
closed=[]
open=[]
path=""
def bfs(goal,path):
    if len(open) != 0:
        start = open.pop(0)
        print(start)
    else:
        return [0, "no path"]
    if start==goal:
        return [1,path]
    else:
        for eachnode in range(len(graphmatrix[start])):
            if graphmatrix[start][eachnode]==1 and eachnode not in closed:
                open.append(eachnode)
                print(open)
        path=path+numtoval[start]+" "
        closed.append(start)
        return bfs(goal,path)
    return [0,"no path"]


while 1:
    edgegiven=input()
    if edgegiven=='done':
        break
    else:
        a,b=list(edgegiven.split(" "))
        edges.append([a,b])
        if valtonum.get(a)==None:
            numtoval[node]=a
            valtonum[a]=node
            node=node+1

        if valtonum.get(b) == None:
            numtoval[node] = b
            valtonum[b] = node
            node=node+1
totalnode=len(list(numtoval.values()))
row=[0]
for i in range(totalnode-1):
    row.extend([0])
for p in range(totalnode):
    graphmatrix.append(row.copy())
for single_edge in edges:
    print(single_edge)
    graphmatrix[valtonum[single_edge[0]]][valtonum[single_edge[1]]]=1
print("Enter start node and end node")
userask=list(input().split(" "))
start=int(valtonum[userask[0]])
goal=int(valtonum[userask[1]])
open.append(start)
print("open",open)
result=bfs(goal,path)
print(result)
if result[0]==1:
    print("Yeah there is a relation and path is:",result[1])
else:
    print("No relation found")
