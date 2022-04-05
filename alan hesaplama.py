print("Geometrik Şekil Türü Belirleme")

sekil=input("Türünü bulmak istediğiniz şekil:")

if sekil=="dörtgen":
    print("dörtgenin kenarlarını giriniz.")
    a=int(input("kenar-1:"))
    b=int(input("kenar-2:"))
    c=int(input("kenar-3:"))
    d=int(input("kenar-4:"))
    if a==b==c==d:
        print("şekliniz kare")
    elif (a==b and c==d) or (a==c and d==b ) or (a==d and b==c):
        print("şekliniz dikdörtgen")
    else:
        print("sekliniz dörtgen.")
elif sekil=="üçgen":
    print("üçgenin kenarlarını giriniz.")
    x=int(input("kenar-1:"))
    y=int(input("kenar-2:"))
    z=int(input("kenar-3:"))
    if  (abs(x-y)<z<x+y and x==y) or (abs(x-y)<z<x+y and x==z) or (abs(x-y)<z<x+y and z==y):
        print("İkizkenar üçgen")

    elif (abs(x-y)<z<x+y) and x==y==z:
        print("Eşkenar Üçgen.")

    elif (abs(x-y)<z<x+y):
        print("Sıradan bir üçgen")
    else:
        print("Üçgen belirtmiyor.")
else:
    print("Geçersiz Şekil")
