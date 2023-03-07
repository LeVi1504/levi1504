a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
p=(a+b+c)/2
import math
if (a,b,c>0):
  if (a+b)>c and (a+c)>c and (b+c)>a:
      print("Dien tich=",round(math.sqrt(p*(p-a)*(p-b)*(p-c)),3))
  else:
    print("Khong hop le")