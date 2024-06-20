def bfs(d,key):
    visited=[]
    q=[key]
    while q:
        for i in d[q[0]]:
            if i not in q and i not in visited:
                q.append(i)
        x=q.pop(0)
        visited.append(x)
    print(visited)

d={
        5:[7,3],
        7:[5,4,3],
        4:[7,8,2],
        8:[3,4,2,10],
        3:[5,7,8],
        2:[4,8,9],
        9:[6,12],
        12:[9],
        6:[9],
        10:[11],
        11:[10,8]
    }

bfs(d,5)










