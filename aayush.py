import math


c = float(input("enter first number = "))

a = input("enter your operation : + - * / , L FOR LOG, T FOR TRIGNOMERTIC (T SHOULD BE IN RADIANS), R FOR UNDERROOT,** FOR POWER =  ")
if a == 'L':
  q = float(input("enter your base"))
  if c>0 and q>0 and q!=1:
      
      print("log base q =", math.log(c,q))
  else :
      print("invalid operation")
elif a == 'R':
  if c>=0:
      print("square root =",math.sqrt(c))
  else :
      print("invalid operation") 

elif a == 'T' :
  print("sin =",math.sin(c))
  print("cos =",math.cos(c))
  print("tan =",math.tan(c))
elif a == '**' :
  d = float(input("enter second number = "))
  print("your answer is =", c**d)
elif a == '+' :
   d = float(input("enter second number = "))
   print("your answer is ",c + d)
elif a =='-':
   d = float(input("enter second number = "))
   print("your answer is ",c-d)
elif a == '*':
   d = float(input("enter second number = "))
   print("your answer is ",c*d)
elif a == '/':
   d = float(input("enter second number = "))
   if d!=0:
       print("your answer is ",c/d)
   else :
      print("cant divide by zero")
elif a == '%':
      d = float(input("enter second number = "))
      print("your answer is ",c%d)
   

   




  
  

