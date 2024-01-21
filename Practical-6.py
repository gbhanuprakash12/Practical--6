fh=open("prac-6.txt",'w')
a=int(input("Enter a:"))
fact=1
while(a>1):
    fact=fact*a
    a=a-1
fh.write('The fact is: '+str(fact)+'\n')
fh.close()