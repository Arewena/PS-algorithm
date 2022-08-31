num=int(input())
for i in range(num):
    a,b=map(int,input().split())
    l=b-a
    n=1
    while n*n<l:
        n+=1
    if n*n-n<l:
        print(2*n-1)
    else:
        print(2*n-2)
        
#포기한 문제