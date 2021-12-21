
# Bankamatik uygulaması...

elif_hesap={
    'ad':"Elif Yılmaz",
    'hesapNo':'124579855116',
    'bakiye':3000,
    'ekHesap':2000

}

ali_hesap={
    'ad':'Ali Turan',
    'hesapNo':'1883272785282',
    'bakiye':2000,
    'ekHesap':1000

}

def para_cek(hesap,miktar):
    print(f"Hoşgeldiniz! {hesap['ad']}")

    if (hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print("Paranızı çekebilirsiniz!")
        bakiyeSorgula(hesap)
    else:
        toplam=hesap['bakiye']+hesap['ekHesap']

        if (toplam>=miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı?(e/h)")

            if ekHesapKullanimi=="e":
                ekhesapKullanilacakMiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-=ekhesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")

        else:
            print("Üzgünüz, bakiyeniz yetersiz.")


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitinizde ise {hesap['ekHesap']} TL bulunmaktadır.")

para_cek(elif_hesap,4000)
print("\n****************************\n")
para_cek(elif_hesap,1000)

