'''
two lists given
[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
1'o clock to 3'o clock
2'o clock to 5'o clock..........
[5,6,5,4,11,2]
1-3 you get 5rupees
2-5 you get 6 rupees
4-6 you get 5 rupees
'''

job=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
pr=[5,6,5,4,11,2]
cp=pr.copy()
for i in range(1,len(job)):
    for j in range(0,i):
        if job[i][0]>=job[j][1]:
            cp[i]=max(cp[j]+pr[i],cp[i])
print(max(cp))
print(cp)
            
    
