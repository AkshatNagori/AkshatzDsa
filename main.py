def firstIndex(arr,x):
  
  if len(arr)==0:
    return -1
  if arr[0]==x:
    return 0
  smallerlistoutput=firstIndex(arr[1:],x)
  if smallerlistoutput==-1:
    return -1
  else:
     return smallerlistoutput+1
  
x=int(input("Enter a no"))
arr=[1,2,3,4,5]

print (firstIndex(arr,x))