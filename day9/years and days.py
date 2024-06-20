'''
consider a year has 360 days
every month has 30 days
every week has 6 days

ip:
    65476 days

op:
    ?y,?m,?w,?d
'''
'''days=65476
year,month,week,day=0,0,0,0
year=days//360
days=days-360*year
month=days//30
days=days-30*month
week=days//6
days=days-6*week
day=days
print(year," year  ",month," months ",week," weeks ",day," days ")
'''
def min_operations_to_move_balls(boxes):
    n = len(boxes)
    answer = [0] * n
    
    # Left to Right pass
    totalBalls = 0
    totalOperations = 0
    for i in range(n):
        answer[i] += totalOperations
        if boxes[i] == '1':
            totalBalls += 1
        totalOperations += totalBalls
    
    # Right to Left pass
    totalBalls = 0
    totalOperations = 0
    for i in range(n-1, -1, -1):
        answer[i] += totalOperations
        if boxes[i] == '1':
            totalBalls += 1
        totalOperations += totalBalls
    
    return answer

# Example usage:
boxes1 = input()

res=min_operations_to_move_balls(boxes1)  
for i in res:
    print(i,end=" ")
