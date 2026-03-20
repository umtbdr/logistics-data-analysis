import pandas as pd
import random
import numpy as np


satir_sayisi = 10000 
limanlar = ["Ambarlı", "İzmir", "Mersin", "Samsun", "İskenderun", "Rotterdam", "Hamburg", "Batum"]
musteriler = ["Arçelik", "Vestel", "Beko", "Şişecam", "Tofaş", "Amazon", "Apple"]
tasima_tipleri = ["Denizyolu", "Karayolu", "Demiryolu"]

data = []

for i in range(satir_sayisi):
    id = f"TRK-{10000 + i}"
    cikis = random.choice(limanlar)
    varis = random.choice([l for l in limanlar if l != cikis])
    musteri = random.choice(musteriler)
    tip = random.choice(tasima_tipleri)
    

    tonaj = random.randint(1000, 45000)
    mesafe = random.randint(200, 5000)
    

    birim_maliyet = random.uniform(1.5, 3.5)
    toplam_maliyet = mesafe * birim_maliyet + (tonaj / 100)
    

    kar_orani = random.uniform(0.1, 0.3)
    satis_fiyati = toplam_maliyet * (1 + kar_orani)
    

    gecikme_gun = random.choice([0, 0, 0, 1, 2, 5])
    
    data.append([id, cikis, varis, musteri, tip, tonaj, mesafe, round(toplam_maliyet, 2), round(satis_fiyati, 2), gecikme_gun])


sutunlar = ["ID", "Cikis", "Varis", "Musteri", "Tip", "Tonaj", "Mesafe", "Maliyet", "Fiyat", "Gecikme"]
df_dev = pd.DataFrame(data, columns=sutunlar)


df_dev.to_csv("Mega_Simulation_Deep_Analysis.csv", index=False)

