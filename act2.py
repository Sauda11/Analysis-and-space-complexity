def sum(n):
        return n*(n+1)/2


print(sum(12))


def arraysum(a):
        sum=0
        for i in a:
                sum=sum+i
        return sum
a=[12,3,4,15] 
print(arraysum(a))



def sum2(n):
        if n<=0:
                return
        return sum2(n-1)   
print(sum2(12))  