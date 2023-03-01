a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a<b<c:
    print("SLN=",c,sep="")
    print("SBN=",a,sep="")
elif a<c<b:
    print("SLN=",b,sep="")
    print("SBN=,a",sep="")
elif b<a<c:
    print("SLN=",c,sep="")
    print("SBN=",b,sep="")
elif b<c<a:
    print("SLN",a,sep="")
    print("SBN=",b,sep="")
elif c<a<b:
    print("SLN=",b,sep="")
    print("SBN=",c,sep="")
elif c<b<a:
    print("SLN=",a,sep="")
    print("SBN=",c,sep="")