n=int(input())
lis=[]
for i in range(n):
    q=list(map(int, input().strip().split(' ')))
    #print("Before Execution: ",i, " - ", q, "list= ", lis)
    if q[0]==1:
        lis.append(q[1])
    if q[0]==2:
        lis.pop(0)
    if q[0]==3:
        print(lis[0])