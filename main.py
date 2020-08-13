print("ax^2+bx+c denkleminin gerçel köklerini bulacağız.")

a = int(input("a değerini girin:"))
b = int(input("b değerini girin:"))
c = int(input("c değerini girin:"))

delta= b**2-(4*a*c)
if(delta<0):
    print("Delta sıfırdan küçük olduğu için denklemin gerçel kökü bulunmamaktadır.")
else:
    x = (-b/(2*a))
    root1 = (x + ((delta)**0.5)/(2/a))
    root2 = (x - ((delta)**0.5)/(2/a))

    print(root1)
    print(root2)
