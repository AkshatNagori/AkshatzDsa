def power(x,n):
  if 0<=x<=8 and 0<=n<=9:
    if x==0:
      return 0
    elif n==0:
      return 1
    else:
      c=1
      
      for i in range(n):
        c = c*x
  return c     
x=int(input("Enter a number:"))
n=int(input("Enter a power:"))
print(power(x,n))
      
      
    
    
