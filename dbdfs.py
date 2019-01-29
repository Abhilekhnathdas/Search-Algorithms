print("Enter the edges if no edges need to be included write 'done'")
graphmatrix=[]
numtoval=dict({})
valtonum=dict({})
node=0
edges=[]
closed=[]
path=""
def dbdfs(start,goal,path,current_state):
    result = [0, path]
    if current_state<=bound:
        path = path + numtoval[start] + " "
        if start==goal:
            result=[1,path]
        else:
            for eachnode in range(len(graphmatrix[start])):
                if graphmatrix[start][eachnode]==1 and eachnode not in closed:
                    closed.append(eachnode)
                    result=dbdfs(eachnode,goal,path,current_state+1)
    return result;


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
print("Enter start node and end node and bound")
userask=list(input().split(" "))
start=int(valtonum[userask[0]])
goal=int(valtonum[userask[1]])
bound=int(userask[2])
closed.append(start)
print(numtoval)
result=dbdfs(start,goal,path,0)
if result[0]==1:
    print("Yeah there is a relation and path is:",result[1])
else:
    print("No relation found",result[1])
