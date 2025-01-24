# Konsol tabanlı hesap makinesi

def toplama(number1, number2):
    return number1 + number2

def fark(number1, number2):
    return number1 - number2

def carpma(number1, number2):
    return number1 * number2

def bolme(number1, number2):
    if number2 == 0:
        return "Hata: Sıfıra bölme yapılamaz!"
    return number1 / number2

def hesap_makinesi():
    while True:
        print("\n******** Hesap Makinesi ********")
        print("Yapmak istediğiniz işlemi seçin:")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Çıkış")

        secim = input("Seçiminiz (1/2/3/4/5): ")

        if secim == '5':
            print("Hesap makinesinden çıkılıyor...")
            break

        if secim in ['1', '2', '3', '4']:
            try:
                number1 = float(input("Birinci sayıyı girin: "))
                number2 = float(input("İkinci sayıyı girin: "))
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")
                continue

            if secim == '1':
                print(f"Sonuç: {toplama(number1, number2)}")
            elif secim == '2':
                print(f"Sonuç: {fark(number1, number2)}")
            elif secim == '3':
                print(f"Sonuç: {carpma(number1, number2)}")
            elif secim == '4':
                print(f"Sonuç: {bolme(number1, number2)}")
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")


hesap_makinesi()
