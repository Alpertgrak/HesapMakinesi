# tkinter modülünü ve messagebox'ı içe aktarıyoruz
import tkinter as tk
from tkinter import messagebox


# Hesap Makinesi Sınıfı
class CalculatorApp:
    def __init__(self, root):
        # Ana pencerenin başlığını "Hesap Makinesi" olarak ayarlıyoruz
        root.title("Hesap Makinesi")

        # Sayı giriş alanları (Entry widget'ları) oluşturuyoruz
        self.entry1 = tk.Entry(root)  # Birinci sayı için giriş alanı
        self.entry1.grid(row=0, column=1, padx=10, pady=10)  # Grid düzeninde konumlandırıyoruz

        self.entry2 = tk.Entry(root)  # İkinci sayı için giriş alanı
        self.entry2.grid(row=1, column=1, padx=10, pady=10)  # Grid düzeninde konumlandırıyoruz

        # Etiketler (Label) oluşturuyoruz
        # "Sayı 1:" etiketi
        tk.Label(root, text="Sayı 1:").grid(row=0, column=0)  # Sayı 1 giriş alanı için etiket
        # "Sayı 2:" etiketi
        tk.Label(root, text="Sayı 2:").grid(row=1, column=0)  # Sayı 2 giriş alanı için etiket
        # "Sonuç:" etiketi, işlemin sonucunu göstermek için kullanılıyor
        self.result_label = tk.Label(root, text="Sonuç: ")  # Sonuç etiketini tanımlıyoruz
        self.result_label.grid(row=2, column=0, columnspan=2)  # Sonucu gösteren etiketi konumlandırıyoruz

        # İşlem butonlarını oluşturuyoruz
        # Toplama butonu
        self.add_button = tk.Button(root, text="Toplama", command=self.Toplama)  # Toplama butonu tanımlanıyor
        self.add_button.grid(row=3, column=0, pady=10)  # Toplama butonu konumlandırılıyor

        # Çıkarma (Fark) butonu
        self.subtract_button = tk.Button(root, text="Fark", command=self.Fark)  # Fark butonu tanımlanıyor
        self.subtract_button.grid(row=3, column=1, pady=10)  # Fark butonu konumlandırılıyor

        # Çarpma butonu
        self.multiply_button = tk.Button(root, text="Çarpma", command=self.Carpma)  # Çarpma butonu tanımlanıyor
        self.multiply_button.grid(row=4, column=0, pady=10)  # Çarpma butonu konumlandırılıyor

        # Bölme butonu
        self.divide_button = tk.Button(root, text="Bölme", command=self.Bolme)  # Bölme butonu tanımlanıyor
        self.divide_button.grid(row=4, column=1, pady=10)  # Bölme butonu konumlandırılıyor

    # Kullanıcıdan giriş alınan sayıları kontrol eder ve float olarak döndürür
    def get_values(self):
        """Sayıları entry alanlarından alır ve float olarak döner"""
        try:
            # Girdiği sayıları alır ve float'a dönüştürür
            number1 = float(self.entry1.get())  # Birinci sayı
            number2 = float(self.entry2.get())  # İkinci sayı
            return number1, number2  # Sayıları döndür
        except ValueError:
            # Sayılar geçerli değilse hata mesajı gösterir
            messagebox.showerror("Geçersiz Giriş", "Lütfen geçerli sayılar girin!")  # Hata mesajı
            return None, None  # Hatalı giriş durumunda None döner

    # Toplama işlemini gerçekleştirir
    def Toplama(self):
        """Toplama işlemi"""
        # Giriş alanlarından sayıları alır
        number1, number2 = self.get_values()
        # Sayılar geçerliyse toplama işlemini yapar
        if number1 is not None and number2 is not None:
            result = number1 + number2  # Sonucu hesapla
            self.result_label.config(text=f"Sonuç: {result}")  # Sonucu etikette göster

    # Çıkarma işlemini gerçekleştirir
    def Fark(self):
        """Çıkarma işlemi"""
        # Giriş alanlarından sayıları alır
        number1, number2 = self.get_values()
        # Sayılar geçerliyse çıkarma işlemini yapar
        if number1 is not None and number2 is not None:
            result = number1 - number2  # Sonucu hesapla
            self.result_label.config(text=f"Sonuç: {result}")  # Sonucu etikette göster

    # Çarpma işlemini gerçekleştirir
    def Carpma(self):
        """Çarpma işlemi"""
        # Giriş alanlarından sayıları alır
        number1, number2 = self.get_values()
        # Sayılar geçerliyse çarpma işlemini yapar
        if number1 is not None and number2 is not None:
            result = number1 * number2  # Sonucu hesapla
            self.result_label.config(text=f"Sonuç: {result}")  # Sonucu etikette göster

    # Bölme işlemini gerçekleştirir
    def Bolme(self):
        """Bölme işlemi"""
        # Giriş alanlarından sayıları alır
        number1, number2 = self.get_values()
        # Sayılar geçerliyse bölme işlemini yapar
        if number1 is not None and number2 is not None:
            # Sıfıra bölme hatasını kontrol eder
            if number2 == 0:
                messagebox.showerror("Bölme Hatası", "Sıfıra bölme yapılamaz!")  # Sıfıra bölme hatası
            else:
                result = number1 / number2  # Sonucu hesapla
                self.result_label.config(text=f"Sonuç: {result}")  # Sonucu etikette göster


# Ana program
if __name__ == "__main__":
    # Ana Tkinter penceresini oluşturuyoruz
    root = tk.Tk()
    # Hesap Makinesi sınıfını başlatıyoruz
    app = CalculatorApp(root)
    # Tkinter uygulamasını başlatıyoruz
    root.mainloop()
