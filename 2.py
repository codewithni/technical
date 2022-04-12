nterms = float('inf')
n = int(input("enter number :- "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("enter number")
elif nterms == 1:
   print("Fibonacci sequence",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
        if ( n1 > n):
           break
        print(n1,end=", ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1