a=float(input(""))
b=float(input(""))
c=float(input(""))
if (a,b,c>0):
    if  a==b and b==c and c==a:  
        print("Tam giac deu")
    elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print("Tam giac vuong")
    elif a+b>c and a+c>b and b+c>a:
        print("Tam giac loai khac")    
    else:
        print("Khong hop le")  