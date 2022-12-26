n=int(input())
a=n
p=0
for i in range(n):
    rem=a%10
    p=p*10+rem*rem
    a=a//10
    a=p
if a>10:
    print('happy')