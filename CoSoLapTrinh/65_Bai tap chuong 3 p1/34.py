t=int(input(""))
l=int(input(""))
h=int(input(""))
dtb=(t*2+l*3+h)/6
if dtb<3:
    print("Kem")
elif 3<=dtb<5:
    print("Yeu")
elif 5<=dtb<6:
    print("Trung binh")
elif 6<=dtb<7:
    print("Trung binh Kha")
elif 7<=dtb<8:
    print("Kha")
elif 8<=dtb<9:
    print("Gioi")
elif 9<=dtb<10:
    print("Xuat sac")