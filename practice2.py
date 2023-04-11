prime =int(input("enter the value"))
count=0 
for  i in range(1, prime+1):
  
  if (prime % i == 0):
   count=count+1
   
print("count =", count)    
if count<=prime and count!=2:
    print("enter number is not a prime number")
else :
      print("enter number is a prime number") 
  
  
  