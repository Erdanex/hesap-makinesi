x = int(input("Lütfen birinci sayıyı girin: "))
y = int(input("Lütfen ikinci sayıyı girin: "))
islem = input("Lütfen yapmak istediğiniz işlemi seçin (+, -, *, /): ")
if islem == "+":
    sonuc = x + y
    print("Sonuç: ", sonuc)
elif islem == "-":
    sonuc = x - y
    print("Sonuç: ", sonuc)
elif islem == "*":
    sonuc = x * y
    print("Sonuç: ", sonuc)
elif islem == "/":
    sonuc = x / y
    print("Sonuç: ", sonuc)
else:
    print("Geçersiz işlem!")
