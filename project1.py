w = int(input("Podaj cyfrę: "))
e = int(input("Podaj cyfrę: "))
print("Podałeś cyfę: ",w, " oraz ", e)
if w > e:
    print(w," Jest większe od ",e)
elif w < e:
    print(w," Jest mniejsze od ",e)
elif w == e:
    print(w," Jest równe ",e)
else:
    print("Musisz podać cyfry")

