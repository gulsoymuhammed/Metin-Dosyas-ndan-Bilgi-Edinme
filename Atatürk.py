class Metin():
    def __init__(self,dosyaAdı):
        with open(dosyaAdı,"r",encoding="utf-8") as file:
            yazi=file.read()
            kelimeListe=yazi.split(" ")
            self.düzenliKelime=list()
            
            for kelime in kelimeListe:
                kelime=kelime.strip("\n")
                kelime=kelime.strip(")")
                kelime=kelime.strip("(")
                kelime=kelime.strip(".")
                kelime=kelime.strip(",")
                kelime=kelime.strip("\"")
                self.düzenliKelime.append(kelime)
            
            
            self.küme=set()
            for i in self.düzenliKelime:
                self.küme.add(i)
             
    def kelimeKümesi(self):
        for i in self.küme:
            print("*************************")
            print(i)
            
    def kacDefa(self):  
       i=0
       kütüphane=dict()

       for i in self.düzenliKelime:
           if(i in kütüphane):
               kütüphane[i]+=1
           else:
               kütüphane[i]=1

       for kelime,sayi in kütüphane.items():
           print("***************************")
           print(f" \"{kelime}\" kelimesinden toplamda {sayi} adet vardir")
           

    def toplamSayilar(self):
        print("********************************************")
        print(f"Metinde geçen toplam kelime sayisi: {len(self.düzenliKelime)}")
        print("********************************************")
        print(f"Metinde geçen birbirinden farklı kelime sayisi: {len(list(self.küme))}")
      
    def kelimeVarMı(self,kelime):
        adet=0
        for i in self.düzenliKelime:
            if(i==kelime):
                adet+=1

        if(adet==0):
            print("****************************************")
            print(f"{kelime} metin içerisinde bulunamadı. ")
        else:
            print("****************************************")
            print(f"\"{kelime}\" kelimesinden metin içerisinde {adet} adet bulundu.")
            


print("************************************************************************")
print("\nLütfen girmek istediğiniz metin belgesini bu projeyle aynı dosyada tutunuz\n")
print("************************************************************************")

dosyaAdi=str(input("Dosya adını .txt uzantısıyla birlikte giriniz.\n"))

metin=Metin(dosyaAdi)



while True:
    print("""
    1.TÜM KELİMELERİN LİSTESİ
    2.TÜM KELİMELERİN4 KÜMESİ 
    3.TÜM KELİMELENİN KAÇ DEFA GEÇTİĞİ
    4.KELİMELERİN SAYI BİLGİLERİ
    5.KELİME VAR MI/YOK MU BİLGİSİ
    q:ÇIKIŞ
    \n
""")
    işlem=input()
    if(işlem=='1'):
        print(metin.düzenliKelime)
    elif(işlem=='2'):
        metin.kelimeKümesi()
    elif(işlem=='3'):
        metin.kacDefa()
    elif(işlem=='4'):
        metin.toplamSayilar()
    elif(işlem=='5'):
        kelime=str(input("Lütfen öğrenmek istediğiniz kelimeyi giriniz:"))
        metin.kelimeVarMı(kelime)
    elif(işlem=='q'):
        break
    else:
        print("Geçersiz işlem.Lütfen girdiğiniz işleme dikkat ediniz.")
        

            


