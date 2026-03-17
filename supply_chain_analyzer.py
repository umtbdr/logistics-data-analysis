import pandas as pd
import matplotlib.pyplot as plt
def veri_yukle(depo):
    try:
       df = pd.read_csv(depo)
       return df
    except FileNotFoundError:
        print("Dosya bulunamadı!")
        return None

df = veri_yukle("Mega_Simulation_Deep_Analysis.csv")
df.info()
df.describe()
def kar_hesabi(liste):
    liste["Kar"] = liste["Fiyat"] - liste["Maliyet"]
    liste["Kar"] = liste["Kar"].round(2)
    return liste

df_kar = kar_hesabi(df)
print(df_kar[["ID","Cikis","Maliyet","Fiyat","Kar"]].head(5))

def varis_tarihi(varis):
    varis["Cikis Tarihi"] = pd.to_datetime("2026-05-07")
    varis["Varis Tarihi"] = varis["Cikis Tarihi"] + pd.to_timedelta(varis["Gecikme"], unit="D")
    return varis

df_zaman = varis_tarihi(df)
print(df_zaman[["ID","Gecikme","Cikis Tarihi","Varis Tarihi"]].head(5))

def istenilen_liste(istek):
    istek1 = (istek["Cikis"] == "İzmir")
    istek2 = (istek["Gecikme"] == 0)
    istek_listesi = istek.loc[istek1 & istek2, ["ID","Cikis","Musteri","Kar","Varis Tarihi"]]
    return istek_listesi

df_istek = istenilen_liste(df)
print(df_istek.head(5))

limanlara_gore_kar = df.groupby("Cikis")["Kar"].sum()
limanlara_gore_kar.to_excel("kar_tablosu.xlsx")
print(limanlara_gore_kar.head(5))
def kar_tablosu(tablo):
    tablo.plot(kind="bar", color=["red", "blue", "green", "orange"])
    plt.title("Limanlara Göre Kâr Dağılımı")
    plt.xlabel("Çıkış Limanı")
    plt.ylabel("Kâr (TL)")
    plt.tight_layout() 
    plt.show()

kar_tablosu(limanlara_gore_kar)
